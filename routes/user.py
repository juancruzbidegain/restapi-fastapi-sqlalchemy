from fastapi import APIRouter

user = APIRouter()

@user.get('/')
def hello_world():
    return {"hola":"mundo"}