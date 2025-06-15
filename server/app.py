from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from server.config import Config

# Initialize Flask extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints
    from server.controllers.restaurant_controller import restaurant_bp
    from server.controllers.pizza_controller import pizza_bp
    from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5555, debug=True) 