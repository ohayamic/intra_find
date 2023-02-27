from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class Todo(BaseModel):
    title: str
    description: str

class SignUp(BaseModel):
    first_name: str
    last_name: str
    email: str
class UpdateSignUp(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]

class GetSignUp(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    first_name: str
    last_name: str
    email: str