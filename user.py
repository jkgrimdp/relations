import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
from organization import OrgSchema

class User(db.Model):
    __tablename__ = "User"
    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String())
    email = db.Column(db.String(), nullable=False, unique=True)
    phone = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    org_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Organization.org_id'), nullable=False)
    active = db.Column(db.Boolean(), default=True)

    def __init__(self, first_name, last_name, email, phone, city, state, org_id, active):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.city = city
        self.state = state
        self.org_id = org_id
        self.active = active

class UserSchema(ma.Schema):
    class Meta:
        fields = ["user_id", "first_name", "last_name", "email", "phone", "city", "state", "org", "active"]
    
    org = ma.fields.Nested(OrgSchema())

user_schema = UserSchema()
users_schema = UserSchema(many=True)


