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
                                        "fieldname": "qty1",
                                        "fieldtype": "Float",
                                        "width": 115
                                },
                                {
                                        "label": _("QTR-1 Amount"),
                                        "fieldname": "amount1",
                                        "fieldtype": "Float",
                                        "width": 105
                                },
                                {
                                        "label": _("QTR-2 Total Qty"),
                                        "fieldname": "qty2",
                                        "fieldtype": "Float",
                                        "width": 115
                                },
                                {
                                        "label": _("QTR-2 Amount"),
                                        "fieldname": "amount2",
                                        "fieldtype": "Float",
                                        "width": 105
                                },
                                {
                                        "label": _("QTR-3 Total Qty"),
                                        "fieldname": "qty3",
                                        "fieldtype": "Float",
                                        "width": 115
                                },
                                {
                                        "label": _("QTR-3 Amount"),
                                        "fieldname": "amount3",
                                        "fieldtype": "Float",
                                        "width": 105
                                },
                                {
                                        "label": _("QTR-4 Total Qty"),
                                        "fieldname": "qty4",
                                        "fieldtype": "Float",
                                        "width": 115
                                },
                                {
                                        "label": _("QTR-4 Amount"),
                                        "fieldname": "amount4",
                                        "fieldtype": "Float",
                                        "width": 105
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
            Ram = 2020-04-01;
            datasales1 =  frappe.db.sql("""
                    SELECT
                            `tabSales Order Item`.item_code,
                            sum(if(`tabSales Order`.`transaction_date` between '{Ram}' and "2020-06-30", qty, 0)),
                            sum(if(`tabSales Order`.`transaction_date` between "2020-04-01" and "2020-06-30", amount, 0)),
                            sum(if(`tabSales Order`.`transaction_date` between "2020-07-01" and "2020-09-30", qty, 0)),
                            sum(if(`tabSales Order`.`transaction_date` between "2020-07-01" and "2020-09-30", amount, 0)),
                            sum(if(`tabSales Order`.`transaction_date` between "2020-10-01" and "2020-12-31", qty, 0)),
                            sum(if(`tabSales Order`.`transaction_date` between "2020-10-01" and "2020-12-31", amount, 0)),
                            sum(if(`tabSales Order`.`transaction_date` between "2021-01-01" and "2021-03-31", qty, 0)),
                            sum(if(`tabSales Order`.`transaction_date` between "2021-01-01" and "2021-03-31", amount, 0))
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
