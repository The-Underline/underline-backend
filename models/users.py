from pydantic import EmailStr, BaseModel


class Users(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class registration_form(Users):
    pass


class registration_response(BaseModel):
    user_id: str


class get_user_info_response(Users):
    pass