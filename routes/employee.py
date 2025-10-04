from datetime import datetime

from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from sqlalchemy import func, select

from db import db
from models.employee import EmployeeModel
from schemas import (
    EmployeePaginationSchema,
    EmployeeSchema,
    EmployeeUpdateSchema,
    SalaryAverageSchema,
)

blp = Blueprint("Employees", __name__, description="Employee operations")


# [POST]
@blp.route("/employees")
class EmployeePost(MethodView):
    @jwt_required()
    @blp.arguments(EmployeeSchema)
    @blp.response(201, EmployeeSchema)
    def post(self, employee_data):
        # Verifico si el email ya esta tomado
        if EmployeeModel.query.filter_by(email=employee_data["email"]).first():
            abort(409, message="Un empleado con ese email ya existe.")
        employee = EmployeeModel(**employee_data)
        try:
            db.session.add(employee)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            abort(500, message=f"Error al crear el empleado: {str(e)}")

        return employee

    # [GET] ALL - Con filtro por posición
    @blp.arguments(EmployeePaginationSchema, location="query")
    @blp.response(200, EmployeeSchema(many=True))
    def get(self, query_args):
        query = select(EmployeeModel)

        if "position" in query_args and query_args["position"]:
            query = query.where(
                EmployeeModel.position.ilike(f"%{query_args['position']}%")
            )

        # Paginación solicitada
        page = query_args.get("page", 1)
        per_page = query_args.get("per_page", 10)
        paginated = db.paginate(query, page=page, per_page=per_page, error_out=False)

        return paginated.items


# [GET] Por ID
@blp.route("/employee/<string:employee_id>")
class Employee(MethodView):
    @jwt_required()
    @blp.response(200, EmployeeSchema)
    def get(self, employee_id):
        employee = EmployeeModel.query.get_or_404(employee_id)
        return employee

    # [DELETE] Por ID
    @jwt_required()
    def delete(self, employee_id):
        employee = EmployeeModel.query.get_or_404(employee_id)
        db.session.delete(employee)
        db.session.commit()
        return {
            "message": f"El empleado {employee.name} {employee.surname} ha sido eliminado."
        }

    # [PUT] Por ID
    @jwt_required()
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


# [GET] Reporte de promedio de salarios
@blp.route("/employees/reports/salary-average")
class SalaryAverage(MethodView):
    @blp.response(200, SalaryAverageSchema)
    def get(self):
        query = select(func.avg(EmployeeModel.salary), func.count(EmployeeModel.id))

        result = db.session.execute(query).one()
        promedio, empleados = result

        if empleados == 0:
            abort(404, message="Empleados insuficientes para el cálculo.")

        return {
            "average_salary": float(promedio) if promedio else 0,
            "total_employees": empleados,
            "report_date": datetime.now(),
        }
