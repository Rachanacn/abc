// Copyright (c) 2023, vehical and contributors
// For license information, please see license.txt

frappe.ui.form.on('MOP Log', 'months', {
	refresh(frm){
		var today = new Date();
		var month = today.toLocaleString('default', { month: 'short' });
		console.log(month);






		// const month = ["January","February","March","April","May","June","July","August","September","October","November","December"];
		// const d = new Date();
		// let months = month[d.getMonth()];
	}
});

	

















		// frm.add_custom_buttom(__("Email"), () => {
		// 	if (frm.doc.__unsaved){
		// 		frappe.throw("save document");
		// 	}
		
		// });


// 		frm.set_query("mop_configuration", () => {
// 			return {
// 				filters: {
// 					company: frm.doc.company,
// 					department: frm.doc.department,
// 					from_date: frm.doc.from_date,
// 					to_date: ['<=', frm.doc.to_date],
// 				}
// 			}
// 		})
// 	},
// });
        
	    // 






// 	mop_configuration(frm){

// 		frappe.call({
// 			method: "vehical.vehical.doctype.mop_log.mop_log.get_child_table",
// 			args:{
// 			"mop_configuration":cur_frm.doc.mop_configuration
// 			},
// 			callback: function(r) {
// 				console.log(r.message);
// 				frm.clear_table('mop');
// 				$.each(r.message, function(i, d) {
// 					var row = frappe.model.add_child(cur_frm.doc, "mop");
// 					row.definition = d.definition;
// 					row.responsipility = d.responsipility;
// 					row.frequency =d.frequency;
// 					row.is_numeric= d.is_numeric;
// 					row.uom = d.uom;
// 					row.target = d.target;
// 					row.is_objective = d.is_objective;
// 					row.target_minimum = d.target_minimum;
// 					row.target_maximum = d.target_maximum;
// 					refresh_field("mop");
// 					});	
                                  


//              }

	    // })


