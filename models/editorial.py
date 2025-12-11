from odoo import models, fields

class Editorial(models.Model):
    _name = 'libreria.editorial'
    _description = 'libreria.editorial'

    name = fields.Char(string='Nombre de la Editorial', required=True)

    libro_ids = fields.One2many(
        'libreria.libro',
        'editorial_id',
        string='Libro Publicados'
    )

    def action_assign_existing_books(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Seleccionar Libros',
            'res_model': 'libreria.libro',
            'view_mode': 'list,form',
            'domain': [('editorial_id', '=', False)],  # o sin filtro
            'context': {'default_editorial_id': self.id},
            'target': 'new',
        }
