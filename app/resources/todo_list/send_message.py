from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flask import request
import datetime
from database.db import mongo
from resources.students.student_proposal import curr_user_is_student


class SendNewMessage(Resource):
    @jwt_required
    def post(self):
        current_user_email = get_jwt_identity()
        body = request.get_json()
        new_todo = None
        inbox = mongo.db.inbox
        messages = mongo.db.messages
        text = body.get('text')
        head = body.get('head')
        if len(text) != 0:
            message_id = messages.insert({
                'head': head,
                'body': text,
                'time': str(datetime.datetime.now().time()),
                'date': str(datetime.datetime.now().date()),
                'is_done': 'false'
            })
            new_todo = messages.find_one({'_id': message_id})
        if curr_user_is_student(current_user_email):
            out = "It's student"
            if new_todo:
                found_inbox = inbox.find_one({'receiver': current_user_email})
                if found_inbox:
                    new_message = new_todo['head'] + ", " + new_todo['body'] + ", " + new_todo['time'] + ", " \
                                  + new_todo['date'] + ", " + new_todo['is_done']
                    found_inbox['messages'].append(new_message)
                    inbox.update({'receiver': current_user_email},
                                 {"$set": {'messages': found_inbox['messages']}})
                    out = new_message
        else:
            out = "It's prof"
        return out
