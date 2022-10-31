<<<<<<< HEAD
from odoo import models, fields


class TravelProfile(models.Model):
    _name = "travel.profile"

    name = fields.Char(string="Traveler Name")
    email = fields.Char(string="Email")
    phone = fields.Char("Phone No")
=======
from odoo import models,fields,api

class Travel(models.Model):
    _name = 'travel.travel'

    name = fields.Char(string='Name')
    destination = fields.Char(char="Destination")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
>>>>>>> 4c74d74b71788ffcc3e3854ac43ee6ac8b05a57c
