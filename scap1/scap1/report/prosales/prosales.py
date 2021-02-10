# Copyright (c) 2013, sprics and contributors
# For license information, please see license.txt

# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
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
			"fieldname":"item",
			"label": _("Item"),
			"fieldtype": "Link",
			"options": "Item",
			"width": 120
		},
		{
			"label": _("Total"),
			"fieldname": "amount",
			"fieldtype": "Float",
			"width": 120
		}
	]
	return columns

def get_data(filters):
	return frappe.db.sql("""
		SELECT
				`tabSales Order Item`.`item_code`,
				`tabSales Order`.amount
		FROM `tabSales Order Item`,`tabSales Order`
		where `tabSales Order Item`.`parent` = `tabSales Order`.`name`
		AND `tabSales Order Item`.`item_code` = %(item)s
		{conditions}
		GROUP BY `tabSales Order Item`.`item_code` """.format(conditions=get_conditions(filters)), filters, as_dict=1)
		def get_conditions(filters) :
	conditions = []

	if filters.get("item"):
		conditions.append(" and `tabSales Order Item`.`item_code`=%(item)s")
	return " ".join(conditions) if conditions else ""
