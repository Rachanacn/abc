# Copyright (c) 2023, vehical and contributors
# For license information, please see license.txt

import frappe

# Filters = frappe._dict
def execute(filters=None):

    columns = get_columns()
    data = get_data(filters)
    return columns, data
    
    # data = frappe.db.sql(
	# """
    #     SELECT
    #        company,
    #        supplier,
    #        supplier_delivery_note,
    #        grand_total
    #     FROM
    #        `tabPurchase Receipt`
    #     WHERE
    #         company=%s
    #         and posting_date between %s and %s
    # """, (filters.get("company"), filters.get("from_date"), filters.get("to_date")), as_dict=1
	# )
 
 
    # return columns, data
 
def get_columns():
	return [
		{
			"label":"Company",
			"fieldname": "company",
			"fieldtype": "Link",
            "options":"Company",
            "width": 150,
		},
  
        {
			"label":"Supplier",
			"fieldname": "supplier",
			"fieldtype": "Data",
			"width": 150,
		},
        {
			"label":"Supplier Delivery Note",
			"fieldname": "supplier_delivery_note",
			"fieldtype": "Data",
			"width": 150,
		},
        {
			"label":"Grand Total",
			"fieldname": "grand_total",
			"fieldtype": "currency",
			"width": 150,
		}
	]
def get_data(filters):
    data = frappe.get_list("Purchase Receipt", {"company": filters.get("company"),
            "posting_date": ["between", filters["from_date"], filters["to_date"]]}, ["company", "supplier", "grand_total", "supplier_delivery_note"])
    # frappe.throw(str(pr))
    # return data
    for i in data:
        i.grand_total += 200
        
    return data
    
