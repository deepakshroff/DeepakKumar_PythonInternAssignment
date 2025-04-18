from app import db, AppModel

sample_apps = [
    AppModel(app_name="WeatherMate", version="1.0.2", description="Weather forecasting app"),
    AppModel(app_name="NoteKeeper", version="2.1", description="App to keep notes organized")
]

db.create_all()
for app in sample_apps:
    db.session.add(app)
db.session.commit()
print("Sample data added!")