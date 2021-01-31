

from odoo import models, fields


class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course Info'

    name = fields.Char(string='Title', required=True)
    discription = fields.Text(string='Description')
    level = fields.Selection([('beginner' , 'Beginner'), ('intermadiate', 'Intermadiate'), ('advance','Advance')])
    active = fields.Boolean(string='Active', default=True)