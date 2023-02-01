# Copyright (c) 2023, vehical and contributors
# For license information, please see license.txt

import frappe
from frappe import _

# def execute(filters=None):
    
# 	data = frappe.db.sql(
# 	"""
# 	SELECT
# 		company vehicle_booking,
# 		employee,
# 		employee_name,
# 		vehicle
# 	FROM
# 		`tabVehicle Booking`
# 	WHERE
# 		company = %s
# 	""", (filters.get("company")), as_dict=1
# 	)

# 	columns = [
# 		_("Vehicle Booking") + ":Link/Company:150",
# 		_("Employee") + ":Data:150",
# 		_("Employee Name") + ":Data:150",
# 		_("Vehicle") + ":Data:150",
# 	]
 
# 	# columns = [
# 	# 	{
# 	# 		"label": "Vehicle Booking",
# 	# 		"fieldname": "company",
# 	# 		"fieldtype": "Data",
# 	# 		"width": 150,
# 	# 	},
# 	# 	{
# 	# 		"label": "Employee",
# 	# 		"fieldname": "employee",
# 	# 		"fieldtype": "Data",
# 	# 		"width": 150,
# 	# 	},
# 	# 	{
# 	# 		"label": "Employee Name",
# 	# 		"fieldname": "employee_name",
# 	# 		"fieldtype": "Data",
# 	# 		"width": 150,
# 	# 	},
# 	# 	{
# 	# 		"label": "Vehicle",
# 	# 		"fieldname": "vehicle",
# 	# 		"fieldtype": "Data",
# 	# 		"width": 150,
# 	# 	}
# 	# ]
 
# 	return columns, data