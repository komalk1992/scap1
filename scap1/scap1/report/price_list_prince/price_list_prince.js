// Copyright (c) 2016, sprics and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Price List Prince"] = {
	"filters": [
		{
			"fieldname":"item_code",
			"label": __("Item"),
			"fieldtype": "Link",
			"options": "Item"
		}

	]
};
