from flask_restx import Resource, Namespace

from app.api_models import course_model, student_model, cours_input
from app.models import Course, Student
from .extensions import db

ns = Namespace("api")

@ns.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}

    
@ns.route("/courses")
class CourseListAPI(Resource):
    @ns.marshal_list_with(course_model) 
    def get(self):
        return Course.query.all()
    
    @ns.expect(cours_input)
    @ns.marshal_with(course_model)
    def post(self):
        cour = Course(name=ns.payload["name"])
        db.session.add(cour)
        db.session.commit()
        return cour
#afch un utilisateur
@ns.route("/courses/<int:id>")
class CourApi(Resource):
    @ns.marshal_with(course_model)
    def get(self,id):
        cour = Course.query.get(id)
        return cour
    #modifier les infos
    @ns.expect(cours_input)
    @ns.marshal_with(course_model)
    def put(self,id):
        cour = Course.query.get(id)
        cour.name = ns.payload["name"]
        db.session.commit()
        return cour
    
    def delete(self,id):
        cour = Course.query.get(id)
        db.session.delete(cour) 
        db.session.commit()
        return {
            "status":True,
            "message":"suppression avec succes"
        }
    







        
        

        
        

    
    
@ns.route("/students")
class StudentAPI(Resource):
    @ns.marshal_list_with(student_model)   
    def get(self):
        return Student.query.all()
    