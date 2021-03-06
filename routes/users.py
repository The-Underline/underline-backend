from pydantic import EmailStr
from config.db import get_database
from fastapi import APIRouter
from starlette.exceptions import HTTPException
from models import users as models
from docs import users as docs
import logging
import util.users as utils

router = APIRouter()

#  C - POST
#  R - GET
#  U - PATCH
#  D - DELETE


@router.post(
    "/users/register",
    response_model=models.registration_response,
    description=docs.registration_desc,
    summary=docs.registration_summ,
    tags=["Users"],
    status_code=201,
)
async def register_user(form: models.registration_form):
    # receive data from client -> util.register method -> return user_id from DB insertion

    # get DB instance
    db = get_database()
    # send the form data and DB instance to util.users.register_user
    user_id = await utils.register_user(form, db)

    # return response in reponse model
    return models.registration_response(user_id=user_id)


@router.delete(
    "/users/delete",
    description=docs.delete_user_desc,
    summary=docs.delete_user_summ,
    tags=["Users"],
    status_code=204,
)
async def delete_user(email: str):

    # if email input is none, raise error
    if not email:
        raise HTTPException(status_code=400,
                            detail="Input invalid/not present")

    # get DB Database
    db = get_database()

    # Delete User
    await utils.delete_user(email, db)


@router.get("/users/find",
            response_model=models.Users,
            description=docs.find_user_by_email_desc,
            summary=docs.find_user_by_email_summ,
            tags=["Users"],
            status_code=201)
async def get_user(email: EmailStr):
    db = get_database()
    user_data = await utils.get_user_info(email, db)
    return models.Users(**user_data)
