# Copyright (c) 2023, vehical and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
#     s=frappe.db.get_value("Fiscal Year",filters.get("fiscal_year"),"year_start_date")
#     e=frappe.db.get_value("Fiscal Year", filters.get("fiscal_year"),"year_end_date")
    columns = get_columns()
    data = get_data(filters)
    return columns, data
    # data=frappe.db.sql(
	# """
    #     SELECT
    #        tml.company,
    #        tml.department,
    #        tmo.measure_si_no,
    #        tmo.measure,
    #        tmo.definition,
    #        tmo.frequency,
    #        tmo.responsipility,
    #        tmo.is_numeric,
    #        tmo.uom,
    #        tmo.target,
    #        tmo.is_objective,
    #        tmo.target_minimum,
    #        tmo.target_maximum
    #     FROM
    #        `tabMOP` tmo
    #     INNER JOIN `tabMOP Log` tml
    #     WHERE
    #         tml.company=%s
    #         and tml.creation between %s and %s
    # """, (filters.get("company"), s, e), as_dict=1
	# )
def get_columns():
    return  [
		{
			"label":"Company",
			"fieldname": "company",
			"fieldtype": "Link",
            "options":"Company",
			"width": 150,
		},
        {
			"label":"Department",
			"fieldname": "department",
			"fieldtype": "Data",
			"width": 150,
		},
        {
			"label":"Fiscal Year",
			"fieldname": "fiscal_year",
			"fieldtype": "Link",
            "options": "Fiscal Year",
			"width": 150,
		},
        {
			"label":"Measure SI No.",
			"fieldname": "measure_si_no",
			"fieldtype": "Data",
			"width": 150,
		},
        {
			
			"label":"Measure",
			"fieldname": "measure",
			"fieldtype": "Data",
			"width": 150,
		},
        {
			
			"label":"Definition",
			"fieldname": "definition",
			"fieldtype": "Small Text",
			"width": 150,
		},
        {
			
			"label":"Frequency",
			"fieldname": "frequency",
			"fieldtype": "Select",
			"width": 150,
		},
        {
		
			
			"label":"Responsipility",
			"fieldname": "responsipility",
			"fieldtype": "Data",
			"width": 150,
		
		},
        {
			"label":"Is Numeric",
			"fieldname": "is_numeric",
			"fieldtype": "Check",
			"width": 150,
		},
        {
			"label":"UOM",
			"fieldname": "uom",
			"fieldtype": "Data",
			"width": 150,
		},
        {
			"label":"Target",
			"fieldname": "target",
			"fieldtype": "Data",
			"width": 150,
		},
        {
			"label":"Is objective",
			"fieldname": "is_objective",
			"fieldtype": "Check",
			"width": 150,
		},
        {
			"label":"Target minimum",
			"fieldname": "target_minimum",
			"fieldtype": "Float",
			"width": 150,
		},
        {
			"label":"Target Maximum",
			"fieldname": "target_maximum",
			"fieldtype": "Float",
			"width": 150,
		},
        {
			"label":"Aug",
            "fieldname": "aug",
			"fieldtype": "Data",
			"width": 150,
		},
        {
			"label":"Sep",
            "fieldname": "sep",
			"fieldtype": "Data",
			"width": 150,
		},
        {
			"label":"Oct",
            "fieldname": "oct",
			"fieldtype": "Data",
			"width": 150,
		},
        {
			"label":"Nov",
            "fieldname": "nov",
			"fieldtype": "Data",
			"width": 150,
		},
        {
			"label":"Dec",
            "fieldname": "dec",
			"fieldtype": "Data",
			"width": 150,
		},
        {
			"label":"Jan",
            "fieldname": "jan",
			"fieldtype": "Data",
			"width": 150,
		}
        
    ]
def get_data(filters):
    data=[]
    
    info=frappe.get_list("MOP Log", pluck="name")
    for i in info:
        # s=frappe.db.get_value("Fiscal Year",filters.get("fiscal_year"),"year_start_date")
        # e=frappe.db.get_value("Fiscal Year", filters.get("fiscal_year"),"year_end_date")
        doc = frappe.get_doc("MOP", i)
        for de in doc.MOP:
            data.append({
                "company": doc.company,
                "department": doc.department,
                "target_maximum": de.target_maximum,
                "target_minimum": de.target_minimum,
                "measure_si_no":de.measure_si_no,
                "measure":de.measure,
                "definition":de.definition,
                "frequency":de.frequency,
                "responsipility":de.responsipility,
                "is_numeric":de.is_numeric,
                "uom":de.uom,
                "target":de.target,
                "is_objective":de.is_objective
            })
    return data

# def add_years(filters):
#     y=frappe.db.get_all("Fiscal Year",fields=["year_start_date","year_end_date"])
#     for i in y:
    
        
#     return y
    