from __future__ import unicode_literals
from frappe import _
import frappe

def execute(self, filters=None):
        columns, data = get_columns(), get_data(filters)
        return columns, data

def get_columns(self):
        if self.filters["range"] == 'Week':
        columns = [
                {
                        "label": _("Item"),
                        "fieldname": "item_code",
                        "fieldtype": "Link",
                        "options": "Item",
                        "width": 150
                },
                {
                        "label": _("Amount"),
                        "fieldname": "amount",
                        "fieldtype": "Float",
                        "width": 120
                }
        ]
        return columns

def get_data(self):
        if self.filters["range"] == 'Week':

        datasales =  frappe.db.sql("""
                SELECT
                        `tabSales Order Item`.item_code,
                        sum(`tabSales Order Item`.amount)
                FROM
                        `tabSales Order Item`,`tabSales Order`
                WHERE
                        `tabSales Order Item`.`parent`=`tabSales Order`.`name`
			AND `tabSales Order`.transaction_date BETWEEN %(from_date)s AND %(to_date)s
                        {conditions}
                GROUP BY
                        `tabSales Order Item`.item_code """.format(conditions=get_conditions(filters)), filters,
as_list=1)

        return datasales

def get_conditions(filters) :
        conditions = []

        if filters.get("item_code"):
                conditions.append(" and `tabSales Order Item`.item_code=%(item_code)s")

        return " ".join(conditions) if conditions else ""
