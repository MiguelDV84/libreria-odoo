from odoo import models, fields, api

class Editorial(models.Model):
    _name = 'libreria.editorial'
    _description = 'Editorial'

    name = fields.Char(string='Nombre de la Editorial', required=True)

    # Relación con libros
    libro_ids = fields.One2many(
        'libreria.libro',
        'editorial_id',
        string='Libros Publicados'
    )

    # Acción del botón
    def action_assign_existing_books(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Seleccionar Libros',
            'res_model': 'libreria.libro',
            'view_mode': 'list,form',
            'domain': [('editorial_id', '=', False)],
            'context': {'default_editorial_id': self.id},
            'target': 'new',
        }