# app/routes.py

from flask import render_template, request, redirect, url_for, jsonify
from app import db  # Import db here after app creation
from app.models import SeasonalFlavor, Cart, Allergen

def register_routes(app):
    # Home Page
    @app.route('/')
    def index():
        return render_template('index.html')

    # Cart Page
    @app.route('/cart', methods=['GET', 'POST'])
    def cart():
        if request.method == 'POST':
            # Get selected flavor and quantity from the form
            flavor_id = request.form['flavor_id']
            quantity = request.form['quantity']
            
            # Fetch the flavor details
            flavor = SeasonalFlavor.query.get(flavor_id)
            
            if flavor:
                # Check if this flavor is already in the cart
                cart_item = Cart.query.filter_by(name=flavor.name).first()
                
                if cart_item:
                    # If already in cart, update quantity
                    cart_item.quantity += int(quantity)
                else:
                    # If not in cart, add a new item
                    new_cart_item = Cart(name=flavor.name, quantity=quantity, price=flavor.price)
                    db.session.add(new_cart_item)
                
                db.session.commit()
                return redirect(url_for('cart'))
        
        # Fetch all cart items
        cart_items = Cart.query.all()
        # Fetch all available seasonal flavors
        flavors = SeasonalFlavor.query.all()
        return render_template('flavor_cart.html', cart_items=cart_items, flavors=flavors)

    # Seasonal Flavors Page
    @app.route('/flavors', methods=['GET', 'POST'])
    def flavors():
        if request.method == 'POST':
            name = request.form['name']
            availability = request.form['availability']
            price = float(request.form['price'])  # Capture the price from the form
            new_flavor = SeasonalFlavor(name=name, availability=availability, price=price)
            db.session.add(new_flavor)
            db.session.commit()
            return redirect(url_for('flavors'))
        
        all_flavors = SeasonalFlavor.query.all()
        return render_template('flavors.html', flavors=all_flavors)

    # Allergens Page
    @app.route('/allergens', methods=['GET', 'POST'])
    def allergens():
        if request.method == 'POST':
            name = request.form['name']
            if Allergen.query.filter_by(name=name).first():
                return jsonify({'error': 'Allergen already exists!'}), 400
            new_allergen = Allergen(name=name)
            db.session.add(new_allergen)
            db.session.commit()
            return redirect(url_for('allergens'))
        
        all_allergens = Allergen.query.all()
        return render_template('allergens.html', allergens=all_allergens)
