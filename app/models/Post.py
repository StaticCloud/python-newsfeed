from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    # user id references the id property of the user model
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship('User')
    # if a post gets deleted, delete all the corresponding comments
    comments = relationship('Comment', cascade='all, delete')

    # as well as the corresponding votes
    votes = relationship('Vote', cascade='all,delete')

    # get the number of every vote object where the post_id equals the corresponding id of the post
    vote_count = column_property(
        select([func.count(Vote.id)]).where(Vote.post_id == id)
    )