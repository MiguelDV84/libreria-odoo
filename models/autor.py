from odoo import models, fields, api

class Autor(models.Model):
    _name = 'libreria.autor'
    _description = 'libreria.autor'
    _rec_name = 'name'

    name = fields.Char(string='Autor', required=True)

    libro_ids = fields.One2many(
        'libreria.libro',
        'autor_id',
        string='Libros'

    )