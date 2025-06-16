from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

app = create_app()
with app.app_context():
    # Add one restaurant
    new_restaurant = Restaurant(name="Test Bistro", address="101 Test Lane")
    db.session.add(new_restaurant)

    # Add one pizza
    new_pizza = Pizza(name="BBQ Chicken", ingredients="Dough, BBQ Sauce, Chicken, Cheese, Onion")
    db.session.add(new_pizza)

    db.session.commit()
    print("Added one restaurant and one pizza!")