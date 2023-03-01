from pymongo import MongoClient
import ssl
from core import config

ssl._create_default_https_context = ssl._create_unverified_context




client = MongoClient("mongodb+srv://root:1234@mongo.7tenj.mongodb.net/test", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

db = client.swe_classroom

collection_name = db["course"]
