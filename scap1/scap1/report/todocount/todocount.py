# Copyright (c) 2013, sprics and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate

def execute(filters=None):

	todo_list = frappe.get_list('ToDo', fields=["name"])

	columns = [_("ID")+":Link/ToDo:90"]

	result = []
	for todo in todo_list:
			result.append([todo.name])

	return columns, result
