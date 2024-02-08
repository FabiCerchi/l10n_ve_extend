from odoo import fields, models, api, _
import json
class ResCountry(models.Model):

    _inherit = "res.country"

    free_zone_domain = fields.Char(compute="_compute_free_zone_domain", readonly=True, store=False,)
    free_zone_ids = fields.Many2many('res.country.state', string="Zonas Francas")

    @api.depends('code')
    def _compute_free_zone_domain(self):
        for rec in self:
            rec.free_zone_domain = json.dumps(
                [('country_id', '=', rec.id),('country_id.code', '=', rec.code)]
            )