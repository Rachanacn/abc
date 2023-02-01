import frappe

def auto_create_vehicle_configuration(doc, action):
    if frappe.db.exists("Vehicle Configuration", {"vehicle": doc.license_plate}):
        frappe.msgprint("Vehicle Configuration already Exists for the Vehicle - {0}".format(frappe.bold(doc.license_plate)))
    else:
        vc = frappe.new_doc("Vehicle Configuration")
        vc.vehicle = doc.license_plate
        vc.mileage = doc.mileage
        vc.odometer_value = doc.last_odometer
        vc.save(ignore_permissions=True)
        
        
        
        
        # apps/vehical/vehical/vehical/utils.py