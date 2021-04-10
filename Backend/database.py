from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Database:

    SQLALCHEMY_DATABASE_URL = f"sqlite:///./portfolio.db"
    # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


    # maak engine
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

    ## hiermee kan sessies gemaakt worden met de engine
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    ## nodig om modellen te maken
    Base = declarative_base()

    @classmethod
    def get_db(cls):
        db = cls.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    @classmethod
    def create_db(cls):
        cls.Base.metadata.create_all(bind=cls.engine)
