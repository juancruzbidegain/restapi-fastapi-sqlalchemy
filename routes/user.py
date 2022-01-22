from fastapi import APIRouter
#conector
from config.db import con
#tabla
from models.user import users

#sqlalchemy
from sqlalchemy import select, func

user = APIRouter()

@user.get('/users')
def get_users():
    #return "Hola" 
    return con.execute(users.select().fetch_all())