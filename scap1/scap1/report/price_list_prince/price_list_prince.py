from __future__ import unicode_literals
from frappe import _
import frappe

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():
	columns = [
		{
			"label": _("Item"),
			"fieldname": "item_code",
			"fieldtype": "Link",
			"options": "Item",
			"width": 150
		},
		{
			"label": _("MRP"),
			"fieldname": "price_list_rate1",
			"fieldtype": "Float",
			"width": 120
		},
		{
			"label": _("Price List Rate"),
			"fieldname": "price_list_rate",
			"fieldtype": "Float",
			"width": 120
		}
	]
	return columns

def get_data(filters):
        datasales =  frappe.db.sql("""
                SELECT
                        `tabItem Price`.item_code,
                        IF(price_list = "MRP",price_list_rate,NULL),
                        IF(%(price_list_rate)s)
                FROM
                        `tabItem Price`
                        {conditions}""".format(conditions=get_conditions(filters)), filters,as_list=1)

        return datasales

def get_conditions(filters) :
	conditions = []

	if filters.get("item_code"):
		conditions.append(" and `tabItem Price`.item_code=%(item_code)s")
	if filters.get("price_list"):
		conditions.append(" and `tabItem Price`.price_list=%(price_list)s")	

	return " ".join(conditions) if conditions else ""