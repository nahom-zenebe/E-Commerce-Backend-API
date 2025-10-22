from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import AnyUrl



class Settings(BaseSettings):
    SECRET_KEY:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    REFRESH_TOKEN_EXPIRE_DAYS:int
    STRIPE_PUBLISHABLE_KEY:str
    STRIPE_SECRET_KEY:str

    MAIL_USERNAME:str
    MAIL_PASSWORD:str
    MAIL_FROM:str
    MAIL_PORT:int
    MAIL_SERVER:str
    MAIL_FROM_NAME:str
    MAIL_STARTTLS:bool=False
    MAIL_SSL_TLS:bool=False
    USE_CREDENTIALS:bool=True
    VALIDATE_CERTS:bool=True


settings=Settings()



