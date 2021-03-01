from __future__ import unicode_literals
import frappe
from frappe import _, scrub
from frappe.utils import getdate, flt, add_to_date, add_days
from six import iteritems
from erpnext.accounts.utils import get_fiscal_year

def execute(filters=None):
        columns, data = get_columns(filters), get_data(filters)
        
        return columns, data
"""
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
                        "label": _("Total Qty"),
                        "fieldname": "qty",
                        "fieldtype": "Float",
                        "width": 100
                },
                {
                        "label": _("Amount"),
                        "fieldname": "amount",
                        "fieldtype": "Float",
                        "width": 100
                }
        ]
        return columns
"""
def get_columns(filters):
        columns = []

        if filters.get('range') == ('Yearly'):
                columns.extend(
                        [
                              {
                                        "label": _("Item"),
                                        "fieldname": "item_code",
                                        "fieldtype": "Link",
                                        "options": "Item",
                                        "width": 150
                                },
                                {
                                        "label": _("Total Qty"),
                                        "fieldname": "qty",
                                        "fieldtype": "Float",
                                        "width": 100
                                },
                                {
                                        "label": _("Amount"),
                                        "fieldname": "amount",
                                        "fieldtype": "Float",
                                        "width": 100
                                }  
                        ]
                )

        if filters.get('range') == ('Quarterly'):
                columns.extend(
                        [
                              {
                                        "label": _("Item"),
                                        "fieldname": "item_code",
                                        "fieldtype": "Link",
                                        "options": "Item",
                                        "width": 150
                                },
                                {
                                        "label": _("QTR-1 Total Qty"),
                                        "fieldname": "qty",
                                        "fieldtype": "Float",
                                        "width": 120
                                },
                                {
                                        "label": _("QTR-1 Amount"),
                                        "fieldname": "amount",
                                        "fieldtype": "Float",
                                        "width": 120
                                }  
                        ]
                )

        return columns

def get_data(filters):
        if filters.get('range') == ('Yearly'):
            
            datasales =  frappe.db.sql("""
                    SELECT
                            `tabSales Order Item`.item_code,
                            sum(`tabSales Order Item`.qty),
                            sum(`tabSales Order Item`.amount)
                    FROM
                            `tabSales Order Item`,`tabSales Order`
                    WHERE
                            `tabSales Order Item`.`parent`=`tabSales Order`.`name`
    			AND `tabSales Order`.transaction_date BETWEEN %(from_date)s AND %(to_date)s
                            {conditions}
                    GROUP BY
                            `tabSales Order Item`.item_code """.format(conditions=get_conditions(filters)), filters, as_list=1)

            return datasales

        if filters.get('range') == ('Quarterly'):
            
            datasales1 =  frappe.db.sql("""
                    SELECT
                            `tabSales Order Item`.item_code,
                            sum(`tabSales Order`.`transaction_date` between "2020-04-01" and "2020-06-30", `tabSales Order Item`.qty, 0),
                            sum(`tabSales Order`.`transaction_date` between "2020-04-01" and "2020-06-30", `tabSales Order Item`.amount, 0)
                    FROM
                            `tabSales Order Item`,`tabSales Order`
                    WHERE
                            `tabSales Order Item`.`parent`=`tabSales Order`.`name`
                AND `tabSales Order`.transaction_date BETWEEN %(from_date)s AND %(to_date)s
                            {conditions}
                    GROUP BY
                            `tabSales Order Item`.item_code """.format(conditions=get_conditions(filters)), filters, as_list=1)

            return datasales1

def get_conditions(filters) :
        conditions = []

        if filters.get("item_code"):
                conditions.append(" and `tabSales Order Item`.item_code=%(item_code)s")

        return " ".join(conditions) if conditions else ""
