from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
db_url = "postgresql://posuser:pospass@localhost:5432/posdb"
engine = create_engine(db_url)

SessionLocal = sessionmaker(autoflush=False, autoCommit = False, bind=engine)