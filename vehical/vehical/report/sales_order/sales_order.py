# Copyright (c) 2023, vehical and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data
#     data = frappe.db.sql(
# 	"""
#         SELECT
#            tso.company,
#            tso.customer,
#            tso.order_type,
#            tso.transaction_date,
#            tso.delivery_date,
#            tsoi.item_code,
#            tsoi.item_name,
#            tsoi.qty,
#            tsoi.rate,
#            tsoi.amount
#         FROM
#            `tabSales Order Item` tsoi
#         INNER JOIN `tabSales Order` tso ON
# 			tso.name = tsoi.parent
#         WHERE
#             tso.company=%s
#             and tso.transaction_date between %s and %s
#     """, (filters.get("company"), filters.get("from_date"), filters.get("to_date")), as_dict=1
# )
def get_columns():
	return [
		{
			"label":"Company",
			"fieldname": "company",
			"fieldtype": "Data",
			"width": 150,
		},
        {
			"label":"Project",
			"fieldname": "project",
			"fieldtype": "Data",
			"width": 150,
		},
        {
			"label":"Sales Order",
			"fieldname": "sales_order",
			"fieldtype": "Data",
			"width": 150,
		},
        
        {
			"label":"Item_code",
			"fieldname": "item_code",
			"fieldtype": "Data",
			"width": 150,
		},
        {
			"label":"Qty",
			"fieldname": "qty",
			"fieldtype": "Data",
			"width": 150,
		}
	]

def get_data(filters):
    data=[]
    info=frappe.get_list("Sales Order", pluck="name")
    for i in info:
        doc = frappe.get_doc("Sales Order", i)
        for items in doc.items:
            data.append({
                "company": doc.company,
                "project": doc.project,
                "sales_order": doc.name,
                "item_code": items.item_code,
                "qty": items.qty
            })
    return data