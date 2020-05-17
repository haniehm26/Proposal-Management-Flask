from pymongo import MongoClient
import gridfs

client = MongoClient()

# initialize the database name
db = client['proposal-management']

# to crate files into database
fs = gridfs.GridFS(db)

# to download files from database
fsb = gridfs.GridFSBucket(db)
