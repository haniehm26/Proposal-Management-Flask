from pymongo import MongoClient
import gridfs

client = MongoClient()
db = client['proposal-management']
fs = gridfs.GridFS(db)
fsb = gridfs.GridFSBucket(db)
