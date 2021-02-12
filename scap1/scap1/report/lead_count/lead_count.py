# Copyright (c) 2013, sprics and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe

#def execute(filters=None):
#	columns, data = [], []
#	return columns, data
def get_columns():
	columns = [
		{
			"label": _("Lead"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Lead",
			"width": 150
		}
	]
	return columns

#	def get_data(filters):
	return frappe.db.sql("""
		SELECT
			COUNT(`tabLead`.name)
		FROM
			`tabLead` """)
