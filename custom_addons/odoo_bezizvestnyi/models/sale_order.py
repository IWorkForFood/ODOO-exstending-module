# -*- coding: utf-8 -*-
"""Расширение модели sale.order (котировки и заказы продаж)."""
import random
import string

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    """Добавляет ответственного за выдачу товара на заказ продажи."""

    _inherit = "sale.order"

    responsible_employee_id = fields.Many2one(
        comodel_name="hr.employee",
        string="Ответственный за выдачу товара",
        required=True,
        check_company=True,
        help="Сотрудник, ответственный за выдачу товара по этому заказу.",
    )

    @api.model
    def _default_new_field(self):
        return "".join(random.choices(string.ascii_letters, k=10))

    new_field = fields.Char(
        string="New Field",
        default=_default_new_field,
        help="Случайный набор из 10 букв при создании",
    )
    new_field_manual_change = fields.Boolean(
        string="New Field Manual Trigger",
        default=False,
        copy=False,
        help="Технический флаг: после первого ручного изменения даты или строк заказa поле New Field вычисляется по формуле.",
    )

    def onchange(self, values, field_names, fields_spec):
        values = dict(values)
        if field_names and ("date_order" in field_names or "order_line" in field_names):
            values["new_field_manual_change"] = True
        return super().onchange(values, field_names, fields_spec)

    # === Автоматическое изменение при смене строк или даты ===
    @api.onchange("order_line", "date_order", "amount_total")
    def _onchange_new_field(self):
        if self.state != "draft":
            return
        if not self.new_field_manual_change:
            return
        if not self.date_order:
            return
        dt_str = self.date_order.strftime("%d/%m/%Y %H:%M:%S")
        self.new_field = f"{dt_str} + {self.amount_total:.2f}"


    # === Ограничение длины + сообщение об ошибке ===
    @api.constrains('new_field')
    def _check_new_field_length(self):
        for record in self:
            if record.new_field and len(record.new_field) > 30:
                raise ValidationError("Длина текста должна быть меньше 30 символов!")

   
