from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from mysql.connector import Error
db_connect = {
      "host":"localhost",
      "user":"root",
      "password":"Jitu@143",
      "database":"zoo"
}

def connect():
       try:
             connect = mysql.connector.connect(**db_connect)
             return connect
       except Error as e:
             print("db not connect",e)



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["https://login-form-theta-rust.vercel.app"],
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
class LoginData(BaseModel):
      userName: str
      password : str
@app.post("/")
def login(user:LoginData):
      print(user.userName)
      print(user.password)
      def insert(u_name,u_password):
            conn = connect()
            cur = conn.cursor()
            try:
               sql = "insert into user(u_name,u_password) values(%s,%s)"
               cur.execute(sql,(u_name,u_password))
               conn.commit()
               print("data stored successfully")
            except Error as e:
                print("data has not stored",e)
            finally:
                  if conn:
                        print("connection close >>>>")
                        cur.close()
                        conn.close()  
      insert(user.userName, user.password)                          
      return{
            "msg":"successfull",
             "data":user
      }
