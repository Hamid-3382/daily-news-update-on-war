# War News Daily

A Flask-based web application for tracking and displaying daily war news updates with advanced search and filtering capabilities.

## Features

- 📰 Browse war news articles with detailed information
- 🔍 Advanced search by keywords, region, country, and severity
- 🌍 Filter by region and affected countries
- ⚠️ Severity levels (Critical, High, Medium, Low)
- 📊 Dashboard statistics showing total news, regions affected, and incident counts
- 💾 SQLite database for persistent storage
- 📱 Responsive design for mobile and desktop
- ⚡ Fast and lightweight Flask framework

## Project Structure

```
war-news-website/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── seed_data.py          # Sample news data for testing
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── style.css         # Styling with dark theme
    └── script.js         # Frontend JavaScript
```

## Installation

1. Navigate to the project directory:
```bash
cd war-news-website
```

2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Seed sample data:
```bash
python seed_data.py
```

5. Run the application:
```bash
python app.py
```

6. Open your browser and visit: `http://localhost:5001`

## API Endpoints

### Get all news with filters
```
GET /api/news?region=Middle%20East&country=Yemen&severity=High&search=ceasefire&sort_by=latest
```

### Get single news article
```
GET /api/news/<id>
```

### Add new news article
```
POST /api/news
Content-Type: application/json

{
  "title": "Breaking News Title",
  "summary": "Brief summary of the news",
  "content": "Full content of the article",
  "region": "Middle East",
  "country": "Yemen",
  "source": "News Agency",
  "severity": "High",
  "image_url": "https://example.com/image.jpg",
  "published_date": "2026-05-01T12:00:00"
}
```

### Update news article
```
PUT /api/news/<id>
Content-Type: application/json
```

### Delete news article
```
DELETE /api/news/<id>
```

### Get filter options
```
GET /api/filters
```

### Get dashboard statistics
```
GET /api/stats
```

## Usage

1. Use the search filters to find news by:
   - Keywords (title, summary, content)
   - Region (Eastern Europe, Middle East, South Asia, etc.)
   - Country
   - Severity level (Critical, High, Medium, Low)

2. Sort results by:
   - Latest first
   - Oldest first
   - By severity level

3. Click "Search" to apply filters
4. Click "Reset" to clear all filters and see all news

## Sample Data

The project includes 10 sample news articles covering various conflict regions:
- Eastern Europe (Ukraine, Moldova)
- Middle East (Yemen, Syria)
- South Asia (Pakistan)
- Sub-Saharan Africa (South Sudan, DRC)
- Global initiatives

## Technologies Used

- **Backend**: Flask, SQLAlchemy
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Python Version**: 3.8+

## Severity Levels

- **Critical**: Immediate threat to civilian populations, major humanitarian crisis
- **High**: Significant military operations, major displacement
- **Medium**: Ongoing operations, diplomatic efforts
- **Low**: Peace initiatives, international cooperation

## Future Enhancements

- Real news API integration (NewsAPI, Guardian API)
- User authentication and saved articles
- Email notifications for breaking news
- Advanced analytics and trend analysis
- Multi-language support
- Social media sharing
- Comment and discussion features
- Admin dashboard for content management

## Disclaimer

This application is for informational and educational purposes only. All news data is fictional sample data for demonstration purposes.
