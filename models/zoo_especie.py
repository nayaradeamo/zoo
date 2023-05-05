from odoo import models,fields
class zoo_especie(models.Model):
    _name ='zoo.especie'
    id = fields.Integer('id', required=True)
    familia = fields.Char ('familia')
    nomcientific = fields.Char('nom cientific')
    nomvulgar = fields.Char('nom vulgar')
    perill = fields.Char('perill extincio')