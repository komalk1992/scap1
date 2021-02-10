# Copyright (c) 2013, sprics and contributors
# For license information, please see license.txt

#from __future__ import unicode_literals
# import frappe

#def execute(filters=None):
#	columns, data = [], []
#	return columns, data


from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate

def execute(filters=None):
	priority_map = {"High": 3, "Medium": 2, "Low": 1}

	todo1_list = frappe.get_list('ToDo1', fields=["name", "date", "description",
		"priority", "reference_type", "reference_name", "assigned_by", "owner"],
		filters={'status': 'Open'})

	todo1_list.sort(key=lambda todo1: (priority_map.get(todo1.priority, 0),
		todo1.date and getdate(todo1.date) or getdate("1900-01-01")), reverse=True)

	columns = [_("ID")+":Link/ToDo1:190", _("Priority22")+"::160", _("Date")+ ":Date",
		_("Description2")+"::150", _("Assigned To/Owner") + ":Data:120",
		_("Assigned By")+":Data:120", _("Reference1")+"::200"]

	result = []
	for todo1 in todo1_list:
		if todo1.owner==frappe.session.user or todo1.assigned_by==frappe.session.user:
			if todo1.reference_type:
				todo1.reference = """<a href="/app/Form/%s/%s">%s: %s</a>""" % (todo1.reference_type,
					todo1.reference_name, todo1.reference_type, todo1.reference_name)
			else:
				todo1.reference = None
			result.append([todo1.name, todo1.priority, todo1.date, todo1.description,
				todo1.owner, todo1.assigned_by, todo1.reference])

	return columns, result
