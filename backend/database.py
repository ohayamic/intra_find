import os
import json
from bson import json_util
import motor.motor_asyncio
from model import Todo, SignUp, GetSignUp
from dotenv import load_dotenv
load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
database = client.SignUpList
collection = database['users']

async def fetch_one_signUp(first_name):
    document = await collection.find_one({"first_name": first_name})
    return document

async def fetch_all_signUps():
    signUps = []
    allSignUps = collection.find({})
    async for doc in allSignUps:
        signUps.append(json.loads(json_util.dumps(doc)))
    return signUps

async def create_signUp(signUp):
    document = signUp
    result = await collection.insert_one(document)
    return document

async def update_signUp(last_name, signUp):
    await collection.update_one({"last_name": last_name}, {"$set": signUp})
    document = await collection.find_one({"last_name": last_name})
    return document

async def remove_signUp(email):
    await collection.delete_one({"email": email})
    return True