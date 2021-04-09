# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Table
# from sqlalchemy.orm import relationship
# from .database import Base
#
#
# class User(Base):
#
#     __tablename__ = 'User'
#     user_id = Column(Integer, primary_key=True)
#     user_title = Column(String(length=50))
#     first_name = Column(String(length=50), nullable=False)
#     last_name = Column(String(length=50), nullable=False)
#     birth_date = Column()
#     phone_number = Column(String(length=15), unique=True)
#     user_email = Column(String(length=50), unique=True)
#     about_me = Column(String)
#     profile_picture = Column(String)
#     login = Column(String(length=30), unique=True, nullable=False)
#     hashed_password = Column(String, nullable=False)
#     is_admin = Column(Boolean, nullable=False)
#     interests = relationship("Interest", order_by="interest", back_populates="user", lazy="joined")
#     address = relationship("Adress", uselist=False, back_populates="user", lazy="joined")
#     work_experiences = relationship("Work_Experience", order_by="desc(job_start_date)", back_populates="user",
#                                     lazy="joined")
#     educations = relationship("Education", order_by="desc(edu_start_date)", back_populates="user", lazy="joined")
#     projects = relationship("Project", order_by="desc(date_start)", back_populates="user", lazy="joined")
#     socials = relationship("Social", back_populates="user", lazy="joined")
#
#     def __str__(self):
#         return self.first_name + " " + self.last_name
#
#
# class Interest(Base):
#
#     __tablename__ = 'Interest'
#
#     interest = Column(String, primary_key=True, length=100)
#     user_id = Column(Integer, ForeignKey('User.user_id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
#     user = relationship("User", back_populates="interests", lazy='joined')
#
#     def __str__(self):
#         return self.interest
#
#
# class Address(Base):
#
#     __tablename__ = 'Address'
#
#     city = Column(String, length=100)
#     street = Column(String, length=100)
#     zip_code = Column(String, length=20)
#     house_number = Column(String, length=100)
#     user_id = Column(Integer, ForeignKey('User.user_id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
#     user = relationship("User", back_populates="address", lazy="joined")
#
#     def __str__(self):
#         return self.street + " " + self.house_number
#
#
# tag_project = Table('tag_project', Base.metadata,
#     Column('tag', String, ForeignKey('Tag.tag')),
#     Column('project_id', Integer, ForeignKey('Project.project_id'))
# )
#
#
# class Project(Base):
#
#     __tablename__ = "Project"
#
#     project_id = Column(Integer, primary_key=True)
#     project_title = Column(String, length=50)
#     live_link = Column(String)
#     github_link = Column(String)
#     date_start = Column(Date)
#     date_end = Column(Date)
#     user_id = Column(Integer, ForeignKey("User.user_id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
#     user = relationship("User", back_populates="projects", lazy="joined")
#     description = relationship("Description", uselist=False, back_populates="project", lazy="joined")
#     tags = relationship("Tag", secondary=tag_project, back_populates="projects", lazy="joined")
#     images = relationship("Image", back_populates="project", lazy="joined")
#
#     def __str__(self):
#         return self.project_title
#
#
# class Description(Base):
#
#     __tablename__ = 'Description'
#
#     short = Column(String)
#     html = Column(String)
#     project_id = Column(Integer, ForeignKey('Project.project_id', onupdate="CASCADE", ondelete="CASCADE"),
#                         nullable=False)
#     project = relationship("Project", back_populates="description", lazy="joined")
#
#
# class Tag(Base):
#
#     __tablename__ = 'Tag'
#
#     tag = Column(String, primary_key=True)
#     category = Column(String, primary_key=True)
#     projects = relationship("Project", secondary=tag_project, back_populates="tags", lazy="joined")
#
#     def __str__(self):
#         return self.technology
#
#
# class Image(Base):
#
#     __tablename__ = "Image"
#
#     image_name = Column(String, primary_key=True)
#     image_url = Column(String)
#     thumbnail = Column(Boolean)
#     project_id = Column(Integer, ForeignKey('Project.project_id', onupdate="CASCADE", ondelete="CASCADE"),
#                         nullable=False)
#     project = relationship("Project", back_populates="images", lazy="joined")
#
#
# class Social(Base):
#
#     __tablename__ = "Social"
#
#     social_name = Column(String, primary_key=True, length=100)
#     social_link = Column(String)
#     user_id = Column(Integer, ForeignKey("User.user_id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
#     user = relationship("User", back_populates="socials", lazy="joined")
#
#     def __str__(self):
#         return self.social_name


from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
