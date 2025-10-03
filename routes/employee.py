from flask.views import MethodView
from flask_smorest import Blueprint

from db import db
from models.employee import EmployeeModel
from schemas import EmployeeSchema, EmployeeUpdateSchema

blp = Blueprint("Employees", __name__, description="Employee operations")


# [POST] & [GET ALL]
@blp.route("/employee")
class EmployeePost(MethodView):
    @blp.arguments(EmployeeSchema)
    @blp.response(201, EmployeeSchema)
    def post(self, employee_data):
        employee = EmployeeModel(**employee_data)
        db.session.add(employee)
        db.session.commit()
        return employee

    @blp.response(200, EmployeeSchema(many=True))
    def get(self):
        return EmployeeModel.query.all()


# [GET] POR ID
@blp.route("/employee/<string:employee_id>")
class Employee(MethodView):
    @blp.response(200, EmployeeSchema)
    def get(self, employee_id):
        employee = EmployeeModel.query.get_or_404(employee_id)
        return employee

    # [DELETE] POR ID
    def delete(self, employee_id):
        employee = EmployeeModel.query.get_or_404(employee_id)
        db.session.delete(employee)
        db.session.commit()
        return {
            "message": f"El empleado {employee.name} {employee.surname} ha sido eliminado."
        }

    # [PUT] POR ID
    @blp.arguments(EmployeeUpdateSchema)
    @blp.response(200, EmployeeSchema)
    def put(self, employee_data, employee_id):
        employee = EmployeeModel.query.get(employee_id)

        if employee:
            employee.name = employee_data["name"]
            employee.surname = employee_data["surname"]
            employee.email = employee_data["email"]
            employee.position = employee_data["position"]
            employee.salary = employee_data["salary"]
        else:
            employee = EmployeeModel(id=employee_id, **employee_data)

        db.session.add(employee)
        db.session.commit()

        return employee
