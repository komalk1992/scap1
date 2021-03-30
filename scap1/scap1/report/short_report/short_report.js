// Copyright (c) 2016, sprics and contributors
// For license information, please see license.txt
/* eslint-disable */
frappe.query_reports["Short Report"] = {
        "filters": 
        [
                {
                        "fieldname":"item_code",
                        "label": __("Item"),
                        "fieldtype": "Link",
                        "options": "Item"
                },
                {
                        "fieldname":"customer",
                        "label": __("Customer"),
                        "fieldtype": "Link",
                        "options": "Customer"
                }
        ]
};