import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    FTP_USER = os.environ['FTP_USER']
    FTP_PASS = os.environ['FTP_PASS']
    FTP_HOST = os.environ['FTP_HOST']

    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']
    DB_HOST = os.environ['DB_HOST']
