// Copyright (c) 2023, vehical and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Department MOP"] = {
	"filters": [
		{
			"label":"Company",
			"fieldname": "company",
			"fieldtype": "Link",
			"options": "Company",
			"reqd":1,
					
		},
		// {
		// 	"label":"Department",
		// 	"fieldname": "department",
		// 	"fieldtype": "Link",
		// 	"options": "Department",
		// 	"reqd":1,

		// },
		{
			"label":"Fiscal Year",
			"fieldname": "fiscal_year",
			"fieldtype": "Link",
			"options": "Fiscal Year",
			"reqd":1,
		},
		
			

	]
};
