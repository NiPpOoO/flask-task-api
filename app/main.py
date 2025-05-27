from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes.task_routes import task_bp

app = Flask(__name__)
app.config.from_object("app.config.Config")

db = SQLAlchemy(app)

app.register_blueprint(task_bp)

if __name__ == "__main__":
    app.run(debug=True)
