// Copyright (c) 2023, vehical and contributors
// For license information, please see license.txt
/* eslint-disable */

// frappe.query_reports["Vehicle Booking"] = {
// 	"filters": [
// 		{
// 			"label": "Company",
// 			"fieldname": "company",
// 			"fieldtype": "Link",
// 			"options": "Company",
// 			"reqd": 1
// 		}
// 	]
// };



import frappe


def execute(filters=None):
    # att=frappe.get_all('Employee')
    # frappe.throw(str(att))
 data = frappe.db.sql(
     """
        SELECT
           ta.company,
           ta.employee,
           ta.employee_name,
           te.department,
           cast(ta.attendance_date AS Date) attn_date,
           te.designation,
           te.employment_type,
           count(*) cnt
        FROM
           `tabAttendance` ta
        INNER JOIN `tabEmployee` te ON
            te.name = ta.employee
        WHERE
            ta.company=%s
            and te.employee=%s
            and ta.attendance_date between %s and %s
            and ta.status = "Absent"
        GROUP BY
            ta.company,
            ta.employee
        
    """, (filters.get("company"),filters.get("employee"), filters.get("from_date"), filters.get("to_date")), as_dict=1
	)

 
 
 
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

	
        {
			"label":"Department",
			"fieldname": "department",
			"fieldtype": "Data",
			"width": 150,
		},
        
        {
			"label":" Attendance Date",
			"fieldname": "attn_date",
			"fieldtype": "Date",
			"width": 150,
		},
        {
			"label":"Designation",
			"fieldname": "designation",
			"fieldtype": "Data",
			"width": 150,
		},
       
        {
			
			"label":"Employment Type",
			"fieldname": "employment_type",
			"fieldtype": "Data",
			"width": 150,
		},
        {
			
			"label":"Count",
			"fieldname": "cnt",
			"fieldtype": "Data",
			"width": 150,
		},
    
        
	]
 return columns , data


#  def check_Consecutive(attendance_date):
#     return sorted(attendance_date) == list(range(min(attendance_date), max(attendance_date)+1))
