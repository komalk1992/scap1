from __future__ import unicode_literals
from frappe import _
import frappe

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():
	columns = [
		{
			"label": _("ID"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Sales Order",
			"width": 150
		},
		{
			"label": _("Customer"),
			"fieldname": "customer",
			"fieldtype": "Link",
			"options": "Customer",
			"width": 120
		},
		{
			"label": _("Item"),
			"fieldname": "item_code",
			"fieldtype": "Link",
			"options": "Item",
			"width": 120
		},
		{
			"label": _("Item Name"),
			"fieldname": "item_name",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Item Group"),
			"fieldname": "item_group",
			"fieldtype": "Link",
			"options": "Item Group",
			"width": 150
		},
		{
			"label": _("Ordered Qty"),
			"fieldname": "qty",
			"fieldtype": "Float",
			"width": 120
		},
		{
			"label": _("Delivered Qty"),
			"fieldname": "delivered_qty",
			"fieldtype": "Float",
			"width": 120
		},
		{
			"label": _("Pendning Qty"),
			"fieldname": "pending_qty",
			"fieldtype": "Float",
			"width": 120
		},
		{
			"label": _("Stock Qty"),
			"fieldname": "actual_qty",
			"fieldtype": "Float",
			"width": 120
		},
		{
			"label": _("Short Qty"),
			"fieldname": "short_qty",
			"fieldtype": "Float",
			"width": 120
		},
	]
	return columns

def get_data(filters):
        datasales =  frappe.db.sql("""
                SELECT
                        `tabSales Order`.name,
                        `tabSales Order`.customer,
                        `tabSales Order Item`.item_code,
                        `tabSales Order Item`.item_name,
                        `tabSales Order Item`.item_group,
                        `tabSales Order Item`.qty,
                        `tabSales Order Item`.delivered_qty,
                        `tabSales Order Item`.qty - `tabSales Order Item`.delivered_qty,
                        `tabSales Order Item`.actual_qty,
                        `tabSales Order Item`.actual_qty - (`tabSales Order Item`.qty - `tabSales Order Item`.delivered_qty)
                FROM
                        `tabSales Order Item`,`tabSales Order`
                WHERE
                        `tabSales Order Item`.`parent`=`tabSales Order`.`name`
                        AND `tabSales Order`.docstatus = 1
                        {conditions}""".format(conditions=get_conditions(filters)), filters,as_list=1)

        return datasales

def get_conditions(filters) :
	conditions = []

	if filters.get("item_code"):
		conditions.append(" and `tabSales Order Item`.item_code=%(item_code)s")
	if filters.get("customer"):
		conditions.append(" and `tabSales Order`.customer=%(customer)s")	

	return " ".join(conditions) if conditions else ""
