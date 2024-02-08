from odoo import fields, models, api, _

class ResPartner(models.Model):

    _inherit = "res.partner"

    is_free_zone = fields.Boolean('Zona Franca', readonly=True, compute="_compute_free_zone")

    @api.depends('country_id','state_id')
    def _compute_free_zone(self):
        for rec in self:
            if rec.state_id and rec.country_id:
                rec.is_free_zone = rec.state_id.id in rec.country_id.free_zone_ids.ids
            else:
                rec.is_free_zone = False