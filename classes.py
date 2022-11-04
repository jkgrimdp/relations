import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma

class Classes(db.Model):
  __tablename__= "Classes"
  class_id = db.Column(UUID(as_uuid=True),True, default=uuid4, unique=True, nullable=False)
  class_name = db.Column(db.String())
  grade = db.Column(db.String())
  users = db.relationship("User", backref="org", lazy=True)

  def __init__(self, class_name, grade):
    self.class_name = class_name
    self.grade = grade

class ClassSchema(ma.Schema):
  class Meta:
    fields = ["class_id", "class_name", "grade"]

class_schema = ClassSchema()
classes_schema = ClassSchema(many=True)