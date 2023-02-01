# Copyright (c) 2023, vehical and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	# att=frappe.get_all('Employee')
	# frappe.throw(str(att))
	data = frappe.db.sql(
		"""
		SELECT
			employee_name,
			employee , 
			Min(AbsentDate) as FromDate,
			Max(AbsentDate) as ToDate, 
			AbsentDays, 
			company
		FROM(
			SELECT 
			employee_name,
			employee,
			AbsentDate,
			company,
			count(*) over(partition by employee,val) as AbsentDays,
			dense_rank() over(partition by Employee order by val) as OrderId
		FROM
			(SELECT 
			employee_name,
			employee,
			company,
			attendance_date as AbsentDate,
			DATE_ADD(attendance_date, INTERVAL -row_number() over(partition by employee order by attendance_date) DAY) as val
		FROM `tabAttendance`
		WHERE 
			status='Absent' 
			and docstatus=1 
			and company=%s 
			and attendance_date BETWEEN %s and %s) as t)as x
		WHERE
			AbsentDays>= 3 
		GROUP BY 
			employee
			
		""", (filters.get("company"), filters.get("from_date"), filters.get("to_date")), as_dict=1
	)
	frappe.throw(str(data))
	columns = [
			{
				"label":"Company",
				"fieldname": "company",
				"fieldtype": "Data",
				"width": 150,
			},
			{
				"label":"Employee",
				"fieldname": "employee",
				"fieldtype": "Data",
				"width": 150,
			},
			{
				"label":"Employee Name",
				"fieldname": "employee_name",
				"fieldtype": "Data",
				"width": 150,
			},

		
			# {
			# 	"label":"Department",
			# 	"fieldname": "department",
			# 	"fieldtype": "Data",
			# 	"width": 150,
			# },
			
			{
				"label":" Attendance Date",
				"fieldname": "attn_date",
				"fieldtype": "Date",
				"width": 150,
			},
			# {
			# 	"label":"Designation",
			# 	"fieldname": "designation",
			# 	"fieldtype": "Data",
			# 	"width": 150,
			# },
		
			# {
				
			# 	"label":"Employment Type",
			# 	"fieldname": "employment_type",
			# 	"fieldtype": "Data",
			# 	"width": 150,
			# },
			{
				
				"label":"Count",
				"fieldname": "AbsentDays",
				"fieldtype": "Data",
				"width": 150,
			},
		
			
		]
	return columns , data


#  def check_Consecutive(attendance_date):
#     return sorted(attendance_date) == list(range(min(attendance_date), max(attendance_date)+1))
