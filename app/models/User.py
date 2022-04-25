from app.db import Base
from sqlalchemy import Column, Integer, String, String
from sqlalchemy.orm import validates

import bcrypt

salt = bcrypt.gensalt()

# User inherits from Base class
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    @validates('email')
    def validate_email(self, key, email):
        # make sure email contains @
        assert '@' in email

        return email
    
    @validates('password')
    def validate_password(self, key, password):
        # make sure password length is greater than 4
        assert len(password) > 4

        return bcrypt.hashpw(password.encode('utf-8'), salt)