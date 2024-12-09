from app import create_app, db
from app.models import SeasonalFlavor, Cart, Allergen

app = create_app()

with app.app_context():
    db.create_all()  # This creates the tables
    print("Database initialized")
