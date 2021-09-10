from sqlalchemy import Boolean, Column, ForeignKey,Integer,String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import true
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=true,index=true)
    email = Column(String,unique=True,index=True)
    hashed_password = Column(String)
    posts = relationship("Posts",back_populates="user")


class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,index=True)
    description =Column(String,index=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    user = relationship("User",back_populates="posts")