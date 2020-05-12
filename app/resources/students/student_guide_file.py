from flask_restful import Resource
from flask import abort, send_from_directory
from database.db import mongo
PATH = r"/static/download_files/pdf"


class GetStudentGuideFile(Resource):
    def get(self):
        try:
            file_name = "HW1.pdf"
            return send_from_directory(PATH, filename=file_name, as_attachment=True)
        except FileNotFoundError:
            abort(404)
