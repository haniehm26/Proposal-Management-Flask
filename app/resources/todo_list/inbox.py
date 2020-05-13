from flask import jsonify
from flask_restful import Resource

from database.db import mongo


class InboxApi(Resource):
    def get(self):
        inbox = mongo.db.inbox
        output = []
        for u in inbox.find():
            output.append({
                'receiver': u['receiver'],
                'sender': u['sender'],
                'messages': u['messages']
            })
        return jsonify({'result': output})
