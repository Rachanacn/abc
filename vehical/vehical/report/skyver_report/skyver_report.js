// Copyright (c) 2023, vehical and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Skyver Report"] = {
	"filters": [
		{
			"label":"Company",
			"fieldname":"company",
			"fieldtype":"Link",
			"options":"Company",
			"reqd":1,
		},
		// {
		// 	"label":"Employee",
		// 	"fieldname":"employee",
		// 	"fieldtype":"Link",
		// 	"options":"Employee",
		// 	"reqd":1,
		// },
		{
			"label":"From Date",
			"fieldname":"from_date",
			"fieldtype":"Date",
			"reqd":1,
		},
		{
			"label":"To Date",
			"fieldname":"to_date",
			"fieldtype":"Date",
			"reqd":1,
		},
		

	]
};
