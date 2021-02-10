# Copyright (c) 2013, sprics and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe

 def get_columns():
	columns = [
		{
			"label": _("Opportunity"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Opportunity",
			"width": 150,
		}
]
	return columns 

 frappe.db.sql("""
		SELECT
			`tabOpportunity`.name
 FROM
			`tabOpportunity`""")
