# Copyright (c) 2023, vehical and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FoodOrdering(Document):
    def validate(self):
        for x in self.get('food_items'):
            x.total_amount = x.quantity * x.rate
        
    
    
    
    
    
    
    
    
    
    
#     def before_save(self):
#         if self.food_menu == "Idly":
#             frappe.db.set_value(self.doctype,self.name,"rate","10")
