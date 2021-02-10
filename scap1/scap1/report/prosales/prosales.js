// Copyright (c) 2016, sprics and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["prosales"] = {
	"filters": [
		{
			"fieldname":"item",
			"label": _("Item"),
			"fieldtype": "Link",
			"options": "Item"
		}
	]
};
