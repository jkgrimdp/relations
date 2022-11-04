import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
from user import User
from organization import Organization
import marshmallow as ma

class UserOrgXref(db.Model):
  __tablename__ = "UserOrgXref"
  relation_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  org_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Organization.org_id'), nullable=False)
  user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('User.user_id'), nullable=False)

  def __init__(self, org_id, user_id):
    self.org_id = org_id
    self.user_id = user_id

class UserOrgXrefSchema(ma.Schema):
  class Meta:
    fields = ['org_id', 'user_id']

user_org_xref_schema = UserOrgXrefSchema()
user_org_xrefs_schema = UserOrgXrefSchema(many=True)


# user_org_xref = Table(
#   "user_org_xref",
#   Base.metadata,
#   Column("user_id", ForeignKey("User.user_id"), primary_key=True)
#   Column("org_id", ForeignKey("Organization.org_id"), primary_key=True)
# )

# class User(Base):
#   __tablename__ = "user_table"
#   id = Column(String, primary_key = True)
#   users = db.relationship("User", secondary=user_org_xref )

# class Organization(Base):
#   __tablename__ = "org_table"
#   id = Column(String, primary_key = True)
#   orgs = db.relationship("Organization", secondary=user_org_xref)