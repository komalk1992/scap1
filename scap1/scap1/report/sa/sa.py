from __future__ import unicode_literals
import frappe
from frappe import _, scrub
from frappe.utils import getdate, flt, add_to_date, add_days
from six import iteritems
from erpnext.accounts.utils import get_fiscal_year

def execute(filters=None):
        return Analytics(filters).run()

        class Analytics(object):
        def __init__(self, filters=None):
                self.filters = frappe._dict(filters or {})
                self.date_field = 'transaction_date' \
                if self.filters.doc_type in ['Sales Order'] else 'posting_date'
                self.months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                self.get_period_date_ranges()

        def run(self):
                self.get_columns()
                self.get_data()
                self.get_chart_data()

                # Skipping total row for tree-view reports
                skip_total_row = 0

                return self.columns, self.data, None, self.chart, None, skip_total_row

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
                        "label": _("Amount"),
                        "fieldname": "amount",
                        "fieldtype": "Float",
                        "width": 120
                }
        ]
                for end_date in self.periodic_daterange:
                        period = self.get_period(end_date)
                        self.columns.append({
                                "label": _(period),
                                "fieldname": scrub(period),
                                "fieldtype": "Float",
                                "width": 100
                        })
        return columns

def get_data(filters):
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
