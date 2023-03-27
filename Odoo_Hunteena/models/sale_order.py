from random import random

from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    test_field = fields.Text(
        string="Test",
        default=random(),
        states={'draft': [('readonly', False)]},
        compute="_compute_test_field",
        store=True
    )

    @api.depends("date_order", "order_line")
    def _compute_test_field(self):
        for record in self:
            record.test_field = f"{record.amount_total:.2f} - {record.date_order}"

    @api.onchange("test_field")
    def _onchange_test_field(self):
        if len(self.test_field) > 50:
            return {'warning': {
                'title': _("Warning"),
                'message': 'Длина текста должна быть меньше 50 символов!'}}
