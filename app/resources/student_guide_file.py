from flask_restful import Resource
from flask import abort, send_from_directory

PATH = r"D:\Uni\Term 6\Software\Project\Project-Flask\app\static\client\pdf"


class GetStudentGuideFile(Resource):
    def get(self):
        try:
            file_name = "HW1.pdf"
            return send_from_directory(PATH, filename=file_name, as_attachment=True)
        except FileNotFoundError:
            abort(404)
