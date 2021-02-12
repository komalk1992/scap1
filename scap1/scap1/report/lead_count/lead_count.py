# Copyright (c) 2013, sprics and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _
import frappe

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

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

def get_data(filters):
	return frappe.db.sql("""
		SELECT
			`tabLead`.name
		FROM
			`tabLead`
		WHERE
			company = %(company)s
			{conditions}
		ORDER BY 
			`tabLead`.creation asc """.format(conditions=get_conditions(filters)), filters, as_dict=1)

def get_conditions(filters) :
	conditions = []

	if filters.get("territory"):
		conditions.append(" and `tabLead`.territory=%(territory)s")

	if filters.get("status"):
		conditions.append(" and `tabLead`.status=%(status)s")
	
	return " ".join(conditions) if conditions else ""
