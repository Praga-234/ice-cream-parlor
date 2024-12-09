# app/models.py

from app import db  # Import db after app is created

# Define models for the application
class SeasonalFlavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    availability = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"SeasonalFlavor('{self.name}', '{self.availability}', {self.price})"


class Cart(db.Model):
    __tablename__ = 'cart'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, default=1, nullable=False)
    price = db.Column(db.Float, nullable=False)
    seasonal_flavor_id = db.Column(db.Integer, db.ForeignKey('seasonal_flavor.id'))  # Foreign key to SeasonalFlavor
    seasonal_flavor = db.relationship('SeasonalFlavor', backref=db.backref('carts', lazy=True))  # Relationship

    def __repr__(self):
        return f"Cart('{self.name}', {self.quantity}, {self.price}, {self.seasonal_flavor.name})"


class Allergen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"Allergen('{self.name}')"
