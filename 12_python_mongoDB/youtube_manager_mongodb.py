import pymongo
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")

client = pymongo.MongoClient(MONGO_URI, tlsAllowInvalidCertificates=True)

db = client["ytmanager"]

video_collection = db["videos"]

# print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, name: {video['name']}, time: {video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(name,time,video_id):
    video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": name, "time": time}})

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("\n Youtubr Manager ")
        print("1. List all videos")
        print("2. add new videos")
        print("3. update videos")
        print("4. delete videos")
        print("5. exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter video id: ")
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            
            update_video(name,time,video_id)
        elif choice == '4':
            video_id = input("Enter video id: ")
            
            delete_video(video_id)

        elif choice == '5':
            break


if __name__ == "__main__":
    main()