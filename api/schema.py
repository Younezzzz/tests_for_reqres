from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    name: str
    job: str
    createdAt: str
    id: str = Field(pattern=r'^\d+$')


class UserItem(BaseModel):
    id: int = Field(gt=0)
    email: EmailStr
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    avatar: str

class ResourceItem(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=1, max_length=100)
    year: int = Field(gt=1900, le=2026)
    color: str = Field(pattern='^#([A-Fa-f0-9]{6})$')
    pantone_value: str = Field(pattern=r'^\d{2}-\d{4}$')

class SingleUser(BaseModel):
    data: UserItem
    support: dict

class UsersListSchema(BaseModel):
    page: int = Field(gt=0)
    per_page: int = Field(gt=0)
    total: int = Field(gt=0)
    total_pages: int = Field(gt=0)
    data: list[UserItem]
    support: dict

class ResourceListSchema(BaseModel):
    page: int = Field(gt=0)
    per_page: int = Field(gt=0)
    total: int = Field(gt=0)
    total_pages: int = Field(gt=0)
    data: list[ResourceItem]

class SingleResource(BaseModel):
    data: ResourceItem
    support: dict



