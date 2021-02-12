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
			"width": 150,
		},
		{
			"label": _("Lead Name"),
			"fieldname": "lead_name",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"fieldname":"status",
			"label": _("Status"),
			"fieldtype": "Data",
			"width": 100
		},
		{
			"fieldname":"lead_owner",
			"label": _("Lead Owner"),
			"fieldtype": "Link",
			"options": "User",
			"width": 100
		},
		{
			"label": _("Territory"),
			"fieldname": "territory",
			"fieldtype": "Link",
			"options": "Territory",
			"width": 100
		},
		{
			"label": _("Source"),
			"fieldname": "source",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Email"),
			"fieldname": "email_id",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Mobile"),
			"fieldname": "mobile_no",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Phone"),
			"fieldname": "phone",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Owner"),
			"fieldname": "owner",
			"fieldtype": "Link",
			"options": "user",
			"width": 120
		},
		{
			"label": _("Company"),
			"fieldname": "company",
			"fieldtype": "Link",
			"options": "Company",
			"width": 120
		}
	]
	return columns

def get_data(filters):
	return frappe.db.sql("""
		SELECT
			`tabLead`.name,
			`tabLead`.lead_name,
			`tabLead`.status,
			`tabLead`.lead_owner,
			`tabLead`.territory,
			`tabLead`.source,
			`tabLead`.email_id,
			`tabLead`.mobile_no,
			`tabLead`.phone,
			`tabLead`.owner,
			`tabLead`.company
		FROM
			`tabLead`
			""", as_dict=1)
