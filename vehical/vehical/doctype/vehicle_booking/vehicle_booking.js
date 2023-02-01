// Copyright (c) 2023, vehical and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vehicle Booking', {
	refresh(frm){
		frm.set_query('employee', () => {
			return {
				filters: {
					user_id: frappe.session.user
				}
			}
		})
	},
	feedback(frm) {
		frappe.call({
			method: "vehical.vehical.doctype.vehicle_booking.vehicle_booking.get_employee",
			args: {
				user: frappe.session.user,
				emp : frm.doc.employee,
			},
		})
	},
	driver(frm){
		frappe.call({
			method: "vehical.vehical.doctype.vehicle_booking.vehicle_booking.get_driver",
			args: {
				user: frappe.session.user,
				driver : frm.doc.driver,
			},
		})
	}
});
