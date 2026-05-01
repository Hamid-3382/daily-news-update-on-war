from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///war_news.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text)
    region = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100))
    source = db.Column(db.String(100))
    severity = db.Column(db.String(50), default='Medium')
    image_url = db.Column(db.String(500))
    published_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'summary': self.summary,
            'content': self.content,
            'region': self.region,
            'country': self.country,
            'source': self.source,
            'severity': self.severity,
            'image_url': self.image_url,
            'published_date': self.published_date.strftime('%Y-%m-%d %H:%M'),
            'created_at': self.created_at.strftime('%Y-%m-%d')
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/news', methods=['GET'])
def get_news():
    region = request.args.get('region', '').lower()
    country = request.args.get('country', '').lower()
    severity = request.args.get('severity', '').lower()
    search = request.args.get('search', '').lower()
    sort_by = request.args.get('sort_by', 'latest')

    query = News.query

    if region:
        query = query.filter(News.region.ilike(f'%{region}%'))
    if country:
        query = query.filter(News.country.ilike(f'%{country}%'))
    if severity:
        query = query.filter(News.severity.ilike(f'%{severity}%'))
    if search:
        query = query.filter(
            (News.title.ilike(f'%{search}%')) |
            (News.summary.ilike(f'%{search}%')) |
            (News.content.ilike(f'%{search}%'))
        )

    if sort_by == 'latest':
        query = query.order_by(News.published_date.desc())
    elif sort_by == 'oldest':
        query = query.order_by(News.published_date.asc())
    elif sort_by == 'severity':
        severity_order = {'Critical': 1, 'High': 2, 'Medium': 3, 'Low': 4}
        query = query.all()
        query = sorted(query, key=lambda x: severity_order.get(x.severity, 5))
        return jsonify([news.to_dict() for news in query])

    news = query.all()
    return jsonify([n.to_dict() for n in news])

@app.route('/api/news/<int:news_id>', methods=['GET'])
def get_news_detail(news_id):
    news = News.query.get_or_404(news_id)
    return jsonify(news.to_dict())

@app.route('/api/news', methods=['POST'])
def add_news():
    data = request.get_json()

    news = News(
        title=data.get('title'),
        summary=data.get('summary'),
        content=data.get('content'),
        region=data.get('region'),
        country=data.get('country'),
        source=data.get('source'),
        severity=data.get('severity', 'Medium'),
        image_url=data.get('image_url'),
        published_date=datetime.fromisoformat(data.get('published_date', datetime.utcnow().isoformat()))
    )

    db.session.add(news)
    db.session.commit()

    return jsonify(news.to_dict()), 201

@app.route('/api/news/<int:news_id>', methods=['PUT'])
def update_news(news_id):
    news = News.query.get_or_404(news_id)
    data = request.get_json()

    news.title = data.get('title', news.title)
    news.summary = data.get('summary', news.summary)
    news.content = data.get('content', news.content)
    news.region = data.get('region', news.region)
    news.country = data.get('country', news.country)
    news.source = data.get('source', news.source)
    news.severity = data.get('severity', news.severity)
    news.image_url = data.get('image_url', news.image_url)

    db.session.commit()

    return jsonify(news.to_dict())

@app.route('/api/news/<int:news_id>', methods=['DELETE'])
def delete_news(news_id):
    news = News.query.get_or_404(news_id)
    db.session.delete(news)
    db.session.commit()

    return '', 204

@app.route('/api/filters', methods=['GET'])
def get_filters():
    regions = db.session.query(News.region).distinct().all()
    countries = db.session.query(News.country).distinct().all()
    severities = db.session.query(News.severity).distinct().all()

    return jsonify({
        'regions': [r[0] for r in regions if r[0]],
        'countries': [c[0] for c in countries if c[0]],
        'severities': [s[0] for s in severities if s[0]]
    })

@app.route('/api/stats', methods=['GET'])
def get_stats():
    total_news = News.query.count()
    regions_count = db.session.query(News.region).distinct().count()
    critical_count = News.query.filter_by(severity='Critical').count()
    high_count = News.query.filter_by(severity='High').count()

    return jsonify({
        'total_news': total_news,
        'regions_affected': regions_count,
        'critical_incidents': critical_count,
        'high_severity': high_count
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
