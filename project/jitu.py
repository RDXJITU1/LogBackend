# app = FastAPI()
# app.add_middleware(
#      CORSMiddleware,
#      allow_origins=["*"],
#      allow_credentials=True,
#      allow_methods=["*"],
#      allow_headers=["*"],
#  )

# class logindata(BaseModel):
#       name: str
#       email:str 
#       password: str 
# @app.post("/login")
# def login(user: logindata):
#       print(user.name)
#       print(user.email)
#       print(user.password) 
#       return {
#            "msg":"login successfull",
#            "data":user
#       }   

