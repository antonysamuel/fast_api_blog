from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from passlib.context import CryptContext
from . import models,schemas

pwd_ctx = CryptContext(schemes=["bcrypt"],deprecated = "auto")


def hash_password(password):
    return pwd_ctx.hash(password)

def verify_password(password,hashed_password):
    return pwd_ctx.verify(password,hashed_password)

def create_user(db:Session,user : schemas.UserCreate):
    db_user = models.User(email = user.email,hashed_password= hash_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print(db_user)
    return db_user

def get_user_by_email(db:Session, email:str):
    return db.query(models.User).filter(models.User.email == email).first()


def authenticate_user(db:Session,email:str,password:str):
    user = get_user_by_email(db,email)
    if not user:
        return False
    if not  verify_password(password,user.hashed_password):
        return False
    return user


def createPost(post: schemas.PostCreate,db:Session):
    
    db_post = models.Posts(title = post.title, description = post.description,user_id = post.uid)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_all_posts(db:Session):
    posts = db.query(models.Posts).all()
    return posts