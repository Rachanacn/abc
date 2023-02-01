frappe.ui.form.on('Employee', {
    refresh(frm){
        frm.add_custom_button(__("Check In"), () =>{
            frappe.call({
                method:"vehical.public.employee.open_check",
                args: {
                    emp:frm.doc.employee,
                    name:frm.doc.employee_name,
                }
            })
        })
    },
    validate(frm) {
        frappe.confirm("ok", () => {
            frm.save();
        })
    }
});