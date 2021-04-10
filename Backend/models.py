from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Table
from sqlalchemy.orm import relationship
from .database import Database

database = Database()


class Admin(database.Base):

    __tablename__ = 'Admin'
    admin_id = Column(Integer, primary_key=True)
    login = Column(String(length=30), unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)


class User(database.Base):

    __tablename__ = 'User'
    user_id = Column(Integer, primary_key=True)
    user_title = Column(String(length=50))
    first_name = Column(String(length=50), nullable=False)
    last_name = Column(String(length=50), nullable=False)
    birth_date = Column(Date)
    phone_number = Column(String(length=15), unique=True)
    user_email = Column(String(length=50), unique=True)
    about_me = Column(String)
    profile_picture = Column(String)
    living_place = Column(String)
    projects = relationship("Project", order_by="desc(Project.date_start)", back_populates="user", lazy="joined")
    socials = relationship("Social", back_populates="user", lazy="joined")

    def __str__(self):
        return self.first_name + " " + self.last_name


tag_project = Table('tag_project', database.Base.metadata,
    Column('tag', String, ForeignKey('Tag.tag')),
    Column('project_id', Integer, ForeignKey('Project.project_id'))
)


class Project(database.Base):

    __tablename__ = "Project"

    project_id = Column(Integer, primary_key=True)
    project_title = Column(String(length=50))
    live_link = Column(String)
    github_link = Column(String)
    date_start = Column(Date)
    date_end = Column(Date)
    user_id = Column(Integer, ForeignKey("User.user_id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="projects", lazy="joined")
    description = relationship("Description", uselist=False, back_populates="project", lazy="joined")
    tags = relationship("Tag", secondary=tag_project, back_populates="projects", lazy="joined")
    images = relationship("Image", back_populates="project", lazy="joined")


class Description(database.Base):

    __tablename__ = 'Description'

    short = Column(String, primary_key=True)
    html = Column(String)
    project_id = Column(Integer, ForeignKey('Project.project_id', onupdate="CASCADE", ondelete="CASCADE"),
                        nullable=False)
    project = relationship("Project", back_populates="description", lazy="joined")


class Tag(database.Base):

    __tablename__ = 'Tag'

    tag = Column(String, primary_key=True)
    category = Column(String)
    projects = relationship("Project", secondary=tag_project, back_populates="tags", lazy="joined")


class Image(database.Base):

    __tablename__ = "Image"

    image_name = Column(String, primary_key=True)
    image_url = Column(String)
    thumbnail = Column(Boolean)
    project_id = Column(Integer, ForeignKey('Project.project_id', onupdate="CASCADE", ondelete="CASCADE"),
                        nullable=False)
    project = relationship("Project", back_populates="images", lazy="joined")


class Social(database.Base):

    __tablename__ = "Social"

    social_name = Column(String(length=100), primary_key=True)
    social_link = Column(String)
    user_id = Column(Integer, ForeignKey("User.user_id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="socials", lazy="joined")
