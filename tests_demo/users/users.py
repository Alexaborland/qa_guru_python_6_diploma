import dataclasses
import datetime
import dotenv
import pydantic_settings


class User(pydantic_settings.BaseSettings):
    gender: str = 'Female'
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str


new_user = User(_env_file=dotenv.find_dotenv('.env'))




#@dataclasses.dataclass
#class User:
 #   gender: str
  #  first_name: str
  #  last_name: str
   # email: str
   # password: str
   # confirm_password: str


#new_user = User(
 #   gender='Female',
  #  first_name='FIRST_NAME',
   # last_name='LAST_NAME',
    #email='EMAIL',
    #password='PASSWORD',
    #confirm_password='CONFIRM_PASSWORD'
#)
