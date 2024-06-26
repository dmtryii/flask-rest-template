
from enum import Enum
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

from app.extensions import db, bcrypt


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'

    def __str__(self):
        return self.value


class BaseUser(db.Model, SerializerMixin):
    # Primary Key
    id = db.Column(db.Integer, primary_key=True)
    
    # User credentials
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    
    # User status
    is_active = db.Column(db.Boolean(), default=True)
    
    # Personal details
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    
    # Registration date
    registration = db.Column(db.DateTime, default=datetime.now, nullable=False)
    
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
    