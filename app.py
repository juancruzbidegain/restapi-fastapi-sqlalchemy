from fastapi import FastAPI

#config project
from routes.user import user

app = FastAPI()

app.include_router(user)


