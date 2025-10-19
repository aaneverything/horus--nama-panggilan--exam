from .config import Config
import os
from flask import Flask
from .extensions import db, migrate, jwt, cors

def create_app() -> Flask:
    
    app = Flask(__name__)
    app.config.from_object(Config)
  
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)

    from .routes import users_bp
    app.register_blueprint(users_bp, url_prefix="/api")

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app
