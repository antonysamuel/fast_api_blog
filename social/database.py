from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB_URL = "postgresql://sam:linux@localhost:5432/fast_api_blog"
DB_URL = "postgresql://leqxcfygqvhafx:f041893837aae65c6e2ed500b23c3eb992892ae224b3f497fb97ee91f1b059b5@ec2-107-22-18-26.compute-1.amazonaws.com:5432/d56uamhdigqlsg"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()