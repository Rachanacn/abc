# Copyright (c) 2023, vehical and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
# from datetime import datetime

class MOPLog(Document):
    pass
    # def validate(self):
    #     to_date= datetime.now()
    #     m = to_date.strftime("%b")
    #     # frappe.throw(str(m))
    #     frappe.db.update(self.doctype,self.name,"months",m)

    # def get_child_table(mop):
    #  cm = frappe.get_value("MOP Log",mop.name,"months")
    #  frappe.db.update("MOP Log",mop.name,"current_month_data",cm.current_month_data)










#      mp= frappe.get_doc("MOP Configuration",mop)
#      for t in mp.get("mop"):
#         			list1.append({
#                'field_1'(b):t.field_1(a),
#         							'field_2'(b):t.field_2(a)
#         						})
#         		return list1

# @frappe.whitelist()
# def get_child_table(mop_configuration):
#     return frappe.db.sql(
# 	"""
# 	select
#  		frequency,
# 		definition,
# 		responsipility,
# 		is_numeric,
# 		uom,
# 		target,
# 		is_objective,
# 		target_minimum,
# 		target_maximum
#    	from 
#     	`tabMOP` 
#     where 
#     	parent = %s
# 	""", (mop_configuration), as_dict=1
# 	)
    
# @frappe.whitelist()
# def send_email(email_address):
# 	frappe.sendmail(recipients=email_address,
# 		subject="Subject of the email",
# 		message= "Content of the email")
