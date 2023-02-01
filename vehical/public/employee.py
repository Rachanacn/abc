import frappe
from frappe.utils import now


@frappe.whitelist()
def open_check(emp,name):
    doc=frappe.new_doc("Employee Checkin")
    doc.employee=emp
    doc.employee_name=name
    doc.log_type="IN"
    doc.save()
    
def validate_emp(doc, action):
    if doc.notice_number_of_days > 90:
        frappe.msgprint("Notice period cannot be greater than 90 days", alert=True, indicator="red")
