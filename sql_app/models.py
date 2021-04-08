from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):

    __tablename__ = 'User'
    user_id = Column(Integer, primary_key=True)
    user_title = Column(String(length=50))
    first_name = Column(String(length=50), nullable=False)
    last_name = Column(String(length=50), nullable=False)
    birth_date = Column()
    phone_number = Column(String(length=15), unique=True)
    user_email = Column(String(length=50), unique=True)
    about_me = Column(String)
    login = Column(String(length=30), unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, nullable=False)
    interests = relationship("Interest", order_by="Interest.interest", back_populates="user", lazy="joined")
    address = relationship("Adress", uselist=False, back_populates="user", lazy="joined")
    work_experiences = relationship("Work_Experience", order_by="desc(job_start_date)", back_populates="user",
                                    lazy="joined")

    def __str__(self):
        return self.first_name + " " + self.last_name


class Interest(Base):

    __tablename__ = 'Interest'

    interest = Column(String, primary_key=True, length=100)
    user_id = Column(Integer, ForeignKey('User.user_id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="interests", lazy='joined')

    def __str__(self):
        return self.interest


class Address(Base):

    __tablename__ = 'Address'

    city = Column(String, length=100)
    street = Column(String, length=100)
    zip_code = Column(String, length=20)
    house_number = Column(String, length=100)
    user_id = Column(Integer, ForeignKey('User.user_id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="address", lazy="joined")

    def __str__(self):
        return self.street + " " + self.house_number


class WorkExperience(Base):

    __tablename__ = 'Work_Experience'

    job_id = Column(Integer, primary_key=True)
    job_title = Column(String, length=50)
    job_description = Column(String)
    job_start_date = Column(String, length=50)
    job_end_date = Column(String, length=50)
    job_employer = Column(String, length=50)
    user_id = Column(Integer, ForeignKey("User.user_id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="work_experiences", lazy="joined")

    def __str__(self):
        return self.job_title + " at " + self.job_employer


class Education(Base):

    __tablename__ = "Education"

    edu_id = mode(primary_key=True)
    edu_name = models.CharField(max_length=100)
    edu_institution = models.CharField(max_length=100)
    edu_start_date = models.CharField(max_length=100)
    edu_end_date = models.CharField(max_length=100, null=True)
    user_id = Column(Integer, ForeignKey("User.user_id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="work_experiences", lazy="joined")

    def __str__(self):
        return self.edu_name + " at " + self.edu_institution


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=50)
    live_link = models.URLField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    date_start = models.CharField(max_length=100)
    date_end = models.CharField(max_length=100, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_title


class Description(models.Model):
    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    short = models.TextField()
    stakeholders = models.TextField()
    problem = models.TextField()
    solution = models.TextField()


class Image(models.Model):
    image = models.ImageField(upload_to='pics')
    thumbnail = models.BooleanField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)


class Tag(models.Model):
    technology = models.CharField(max_length=100)
    project = models.ManyToManyField(Project)

    def __str__(self):
        return self.technology




class Social(models.Model):
    social_name = models.CharField(max_length=100, primary_key=True)
    social_link = models.URLField(null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.social_name
