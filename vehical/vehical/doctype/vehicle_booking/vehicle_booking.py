# Copyright (c) 2023, vehical and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class VehicleBooking(Document):
    def on_submit(self):
        if self.workflow_state == "Trip Completed":
            if not self.current_odometer_value:
                frappe.throw("current odometer value cannot be zero")  
            else:
                vc = frappe.get_doc("Vehicle Configuration", {"vehicle": self.vehicle})
                if float(self.current_odometer_value) <= float(vc.odometer_value):
                    frappe.throw("Current Odometer Value cannot be less than/same as Last Odometer Value")
                else:
                    frappe.db.update("Vehicle Configuration", vc.name, "odometer_value", self.current_odometer_value)
                    
            emp = frappe.get_value("Driver", self.driver, "employee")
            emp_name = frappe.get_value("Employee", emp, "employee_name")
            attendance_req = frappe.new_doc("Attendance Request")
            attendance_req.employee = emp
            attendance_req.employee_name = emp_name
            attendance_req.company = self.company
            attendance_req.from_date = self.from_date
            attendance_req.to_date = self.to_date
            attendance_req.reason = "On Duty"
            attendance_req.explanation = self.purpose
            attendance_req.save()
            frappe.db.update("Vehicle Booking", self.name, "attendance_request", attendance_req.name)  
            
    def validate(self):
        if self.pick_up and self.drop:
            frappe.throw("Pick Up & Drop cannot be selected at a time")
        if not self.pick_up and not self.drop:
            frappe.throw("Pick Up & Drop cannot be empty at a time")
        # calculate(self.odometer)

@frappe.whitelist()
def get_employee(user, emp):
    # if emp != frappe.get_value("Employee", {"user_id": user}, "name"):
    #     frappe.throw()
    employee = frappe.get_doc("Employee", {"user_id": user})
    if emp != employee.name:
        frappe.throw("Feedback can only be edited by - {0}".format(frappe.bold(employee.employee_name)))
    
@frappe.whitelist()
def get_driver(user, driver):
    employee = frappe.get_doc("Employee", {"user_id": user})
    if driver != employee.name:
        frappe.throw("Current Odometer Value can only be edited by the Driver - {0}".format(frappe.bold(employee.employee_name)))
    
# def calculate(a)