from sqlalchemy import func

import db


class EmployeeModel(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    surname = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False, index=True)
    position = db.Column(db.String(50), nullable=False, index=True)
    salary = db.Column(db.Numeric(12, 2), nullable=False)
    hire_date = db.Column(db.Date, nullable=False, server_default=func.current_date())
