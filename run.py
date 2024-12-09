from app import create_app, db
from app.models import SeasonalFlavor, Cart, Allergen

app = create_app()

with app.app_context():
    # Create all tables manually
    db.create_all()
    print("Tables created successfully!")

if __name__ == "__main__":
    app.run(debug=True)
