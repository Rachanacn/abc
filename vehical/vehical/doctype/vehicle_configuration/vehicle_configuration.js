// Copyright (c) 2023, vehical and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vehicle Configuration', {
	before_save(frm){
		var tot_amnt = 0;
		for(let index = 0; index < frm.doc.refueling_details.length; index++){
			tot_amnt += frm.doc.refueling_details[index].amount;
		}
		frm.set_value('total_amount_spend', tot_amnt);
		frm.refresh_field('total_amount_spend');
	}
});

frappe.ui.form.on('Refueling Details', {
	fuel_unit_rate(frm, cdt, cdn) {
		let row = locals[cdt][cdn];
		frappe.model.set_value(cdt, cdn, 'amount', row.fuel_qty * row.fuel_unit_rate);
		frm.refresh_field('amount');
	}
});