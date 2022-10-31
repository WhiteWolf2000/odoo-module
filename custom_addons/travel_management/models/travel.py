from odoo import models, fields


class TravelProfile(models.Model):
    _name = "travel.profile"

    name = fields.Char(string="Traveler Name")
    email = fields.Char(string="Email")
    phone = fields.Char("Phone No")
