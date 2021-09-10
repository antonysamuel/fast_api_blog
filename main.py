from fastapi import FastAPI,HTTPException,status
from fastapi.params import Depends
from sqlalchemy.sql.functions import mode
from social.database import SessionLocal,engine
from sqlalchemy.orm import Session
from social import schemas,models,curd
from fastapi.middleware.cors import CORSMiddleware
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/register',response_model=schemas.UserResp)
def register(req: schemas.UserCreate,db : Session = Depends(get_db)):
    user = curd.get_user_by_email(db,req.email)
    if user:
        raise HTTPException(status_code=status.HTTP_302_FOUND,detail="Email already registered")
    return curd.create_user(db,req) 

@app.post('/login',response_model=schemas.User)
def login(req: schemas.UserCreate,db : Session = Depends(get_db)):
    user = curd.authenticate_user(db,req.email,req.password)
    if user == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    return user

@app.post('/postblog')
def postblog(req: schemas.PostCreate,db : Session = Depends(get_db)):
    return curd.createPost(req,db)

@app.get('/blog/{id}')
def getBlog(id: int,db : Session = Depends(get_db)):
    pass

@app.get('/')
def home(db: Session = Depends(get_db)):
    posts = {
        'post_data' : curd.get_all_posts(db)
    }
    return posts