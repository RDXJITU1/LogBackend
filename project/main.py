from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

class logindata(BaseModel):
      name:str
      email:str
@app.post("/")
def login(user:logindata):
      print(user.name)
      print(user.email)
      return{
            "msg":"succes",
            "daTA":user
      }      