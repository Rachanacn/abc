// Copyright (c) 2023, vehical and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicle Parking",function(frm){
        var date1 = new Date(frm.doc.from_time);
    var date2 = new Date(frm.doc.to_time);
    var Difference_In_Time = date2.getTime() - date1.getTime();
    frm.doc.total_time = Difference_In_Time / (1000 * 60);

    }
);
