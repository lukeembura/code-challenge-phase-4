from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()
with app.app_context():
    # Add one restaurant
    new_restaurant = Restaurant(name="Test Bistro", address="101 Test Lane")
    db.session.add(new_restaurant)

    # Add one pizza
    new_pizza = Pizza(name="BBQ Chicken", ingredients="Dough, BBQ Sauce, Chicken, Cheese, Onion")
    db.session.add(new_pizza)

    # Commit to get IDs
    db.session.commit()

    # Create connection between restaurant and pizza
    restaurant_pizza = RestaurantPizza(
        price=15,
        restaurant_id=new_restaurant.id,
        pizza_id=new_pizza.id
    )
    db.session.add(restaurant_pizza)
    db.session.commit()
    print("Added one restaurant, one pizza, and connected them!")