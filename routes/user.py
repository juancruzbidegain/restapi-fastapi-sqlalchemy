from fastapi import APIRouter
#conector
from config.db import con
#tabla
from models.user import users

#sqlalchemy
from sqlalchemy import select, func


#schemas
from schemas.user  import User



from cryptography.fernet import Fernet


user = APIRouter()


key = Fernet.generate_key()
f = Fernet(key)

@user.get('/users')
def get_users():
    return con.execute(users.select()).fetchall()


@user.post('/users')
def create_users(user: User):
    new_user = dict(user)
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    execute_insert = con.execute(users.insert().values(new_user))
    print(execute_insert.lastrowid)
    return con.execute(users.select().where(users.c.id == execute_insert.lastrowid)).first()

@user.get('/users/{id}')
def get_user(id : str):
    return con.execute(users.select().where(users.c.id == id)).first()
