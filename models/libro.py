from odoo import models, fields, api
from datetime import date

class Libreria(models.Model):
    _name = 'libreria.libro'
    _description = 'libreria.libro'
    _rec_name = 'name'

    name = fields.Char(string='Nombre')
    libro_description = fields.Text(string='Descripción')
    portada = fields.Image(max_width=100, max_height=100)
    pages = fields.Integer(string='Páginas')
    price = fields.Float(string='Precio')
    is_available = fields.Boolean(string='Disponible', default=True)
    publication_date = fields.Date(string='Fecha de Publicación')
    created_datetime = fields.Datetime(string='Creado el')
    date_since_publication = fields.Integer(string='Días desde Publicación', compute='_compute_days')
    #Relacion ManyToMany
    autores_ids = fields.Many2many(
        'libreria.autor',
        string='Autores'
    )
    #Relacion ManyToOne
    editorial_id = fields.Many2one(
        'libreria.editorial',
        string='Editorial')

    @api.depends('publication_date')
    def _compute_days(self):
        for record in self:
            if record.publication_date:
                record.date_since_publication = (date.today() - record.publication_date).days
            else:
                record.date_since_publication = 0
