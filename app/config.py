import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    DEBUG = True
