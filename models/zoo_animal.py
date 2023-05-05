from odoo import models,fields
class zoo_animal(models.Model):
    _name ='zoo.amimal'
    id = fields.Integer('id', required=True)
    continentorigen = fields.Char ('contient d_origen')
    datanaix = fields.Date('data de naixement')
    paisorigen = fields.Char('pais d_origen')
    sexe = fields.Char('sexe')