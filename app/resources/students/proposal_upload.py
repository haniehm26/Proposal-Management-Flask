from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flask import jsonify

from database.file_handler import fs
from database.db import mongo
from resources.students.student_proposal import curr_user_is_student
import datetime


class ProposalUpload(Resource):
    @jwt_required
    def get(self):
        current_user_email = get_jwt_identity()
        out = "NONE"
        if curr_user_is_student(current_user_email):
            students = mongo.db.students
            student = students.find_one({'email': current_user_email})
            if student:
                proposal = {'title_persian': student['proposal_document_title_persian'],
                            'title_english': student['proposal_document_title_english'],
                            'keywords_persian': student['proposal_document_keywords_persian'],
                            'keywords_english': student['proposal_document_keywords_english'],
                            'type': student['proposal_document_type'],
                            'supportive_reference': student['proposal_document_supportive_reference'],
                            'how_to_solve': student['proposal_document_how_to_solve'],
                            'is_new': student['proposal_document_is_new'],
                            'assumption': student['proposal_document_assumption'],
                            'definition': student['proposal_document_definition'],
                            'history': student['proposal_document_history'],
                            'tools': student['proposal_document_tools'],
                            'references': student['proposal_document_references'],
                            'references_other_languages': student['proposal_document_references_other_languages'],
                            'time_table': student['proposal_document_time_table'],
                            'upload_date': datetime.datetime.now().date(),
                            'upload_time': datetime.datetime.now().time()
                            }

                proposal_file = fs.new_file(filename=student['info_student_id'], encoding='utf-8')
                for key, val in proposal.items():
                    proposal_file.write(key + '\n' + str(val) + '\n\n')
                proposal_file.close()
                out = "Successful"
            else:
                out = "Student not found"
        else:
            out = "It's prof"

        return jsonify({'out': out})
