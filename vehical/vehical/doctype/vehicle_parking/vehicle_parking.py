# Copyright (c) 2023, vehical and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now
# from datetime import datetime


class VehicleParking(Document):
    def on_submit(self):
        # rs=10
        # rss=30
        # total_time=self.from_time - self.to_time
        if self.vehicle_type == "2 wheeler":
            frappe.db.update(self.doctype,self.name,"amount","10")
        elif self.vehicle_type == "4 wheeler":
            frappe.db.update(self.doctype,self.name,"amount","30")
    
        # frappe.db.update(self.doctype,self.name,"total_time",total_time)
            
            
    # def before_save(self):
    #     fr = datetime.strptime(self.from_time, "%Y-%m-%d %H:%M:%S")
    #     to = datetime.strptime(self.to_time, "%Y-%m-%d %H:%M:%S")
    #     diff = to - fr
    #     minutes = round(diff.total_seconds()/60,0)
    #     self.total_time = minutes
    #     # frappe.db.set_value(self.doctype,self.name,"total_time",minutes)

        
        
        
        
        # fr =  datetime.strptime(self.from_time,"%d/%m/%Y %H:%M:%S")
        # frappe.throw(str(fr))
        # to = datetime.strptime(self.to_time,"%d/%m/%Y %H:%M:%S")
        # time_diff_in_hours =  fr - to
        # frappe.throw(str(time_diff_in_hours))
        # seconds = time_diff_in_hours.total_seconds()
        # # minutes = seconds / 60
        ##frappe.db.update(self.doctype,self.name,"total_time",seconds)
        
        
    def after_save(self):
        # total_time=self.from_time + self.to_time
        frappe.db.update(self.doctype,self.name,"to_time",now()) 
        # frappe.db.update(self.doctype,self.name,"total_time",total_time)
         
        # frappe.set_value(self.doctype,"total_time",self.from_time+self.to_time)