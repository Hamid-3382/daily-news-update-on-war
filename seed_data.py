from app import app, db, News
from datetime import datetime, timedelta

sample_news = [
    News(
        title='Military Operations Intensify in Eastern Region',
        summary='Armed forces report increased military activity and strategic movements in the eastern conflict zone.',
        content='Recent reports indicate a significant escalation in military operations across the eastern region. Multiple sources confirm increased troop movements and artillery exchanges. Humanitarian organizations express concern over civilian displacement.',
        region='Eastern Europe',
        country='Ukraine',
        source='International News Agency',
        severity='High',
        published_date=datetime.utcnow() - timedelta(hours=2)
    ),
    News(
        title='Ceasefire Negotiations Resume in Middle East',
        summary='International mediators meet to discuss peace terms and humanitarian corridors in the ongoing conflict.',
        content='Diplomatic efforts continue as international mediators convene for the third round of peace negotiations. Both parties have agreed to discuss humanitarian aid distribution and civilian evacuation routes.',
        region='Middle East',
        country='Yemen',
        source='Global Peace Initiative',
        severity='Medium',
        published_date=datetime.utcnow() - timedelta(hours=4)
    ),
    News(
        title='Critical Humanitarian Crisis Declared',
        summary='UN agencies warn of severe food shortages and medical supply shortages affecting millions of civilians.',
        content='The United Nations has declared a critical humanitarian crisis in the affected region. Over 5 million people are facing acute food insecurity. Medical facilities are overwhelmed and running low on essential supplies.',
        region='Sub-Saharan Africa',
        country='South Sudan',
        source='UN Humanitarian Affairs',
        severity='Critical',
        published_date=datetime.utcnow() - timedelta(hours=1)
    ),
    News(
        title='Border Tensions Escalate Between Nations',
        summary='Military buildup reported along disputed border as diplomatic tensions reach new heights.',
        content='Intelligence reports confirm significant military deployment along the disputed border region. Both nations have mobilized additional forces. International observers are monitoring the situation closely.',
        region='South Asia',
        country='Pakistan',
        source='Defense Ministry',
        severity='High',
        published_date=datetime.utcnow() - timedelta(hours=6)
    ),
    News(
        title='Refugee Crisis Worsens as Displacement Continues',
        summary='Hundreds of thousands flee conflict zones seeking safety in neighboring countries.',
        content='Refugee camps are overwhelmed as displacement continues. Aid organizations report insufficient resources to handle the influx. Border nations struggle to accommodate the growing refugee population.',
        region='Middle East',
        country='Syria',
        source='Refugee Council',
        severity='High',
        published_date=datetime.utcnow() - timedelta(hours=3)
    ),
    News(
        title='International Coalition Launches Humanitarian Mission',
        summary='Multiple nations coordinate efforts to deliver emergency aid and medical assistance to affected populations.',
        content='An international coalition has launched a coordinated humanitarian mission. Airlifts of medical supplies and food aid are underway. Multiple NGOs are working alongside government agencies.',
        region='Eastern Europe',
        country='Moldova',
        source='International Coalition',
        severity='Medium',
        published_date=datetime.utcnow() - timedelta(hours=5)
    ),
    News(
        title='Cyber Attacks Reported During Conflict',
        summary='Critical infrastructure targeted by coordinated cyber operations affecting civilian services.',
        content='Cybersecurity experts report sophisticated cyber attacks targeting critical infrastructure. Power grids, water systems, and communication networks have been affected. International cyber security teams are responding.',
        region='Eastern Europe',
        country='Ukraine',
        source='Cyber Security Agency',
        severity='Critical',
        published_date=datetime.utcnow() - timedelta(hours=7)
    ),
    News(
        title='Peace Summit Scheduled for Next Month',
        summary='World leaders announce plans for comprehensive peace summit to address regional conflicts.',
        content='The United Nations has announced a comprehensive peace summit scheduled for next month. All parties have been invited to participate. International observers will monitor the proceedings.',
        region='Global',
        country='Switzerland',
        source='UN Secretary General',
        severity='Low',
        published_date=datetime.utcnow() - timedelta(hours=8)
    ),
    News(
        title='Economic Sanctions Imposed on Aggressor Nation',
        summary='International community implements comprehensive economic sanctions in response to military aggression.',
        content='The international community has unanimously voted to impose comprehensive economic sanctions. Trade restrictions and asset freezes have been implemented. Financial institutions are complying with the sanctions regime.',
        region='Eastern Europe',
        country='Russia',
        source='International Economic Council',
        severity='High',
        published_date=datetime.utcnow() - timedelta(hours=9)
    ),
    News(
        title='War Crimes Investigation Launched',
        summary='International Criminal Court opens investigation into alleged violations of international humanitarian law.',
        content='The International Criminal Court has launched a formal investigation into alleged war crimes. Evidence is being collected from multiple sources. Witnesses are being interviewed by ICC investigators.',
        region='Sub-Saharan Africa',
        country='Democratic Republic of Congo',
        source='International Criminal Court',
        severity='High',
        published_date=datetime.utcnow() - timedelta(hours=10)
    ),
]

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.query(News).delete()
        db.session.add_all(sample_news)
        db.session.commit()
        print(f'Added {len(sample_news)} news articles to database')
