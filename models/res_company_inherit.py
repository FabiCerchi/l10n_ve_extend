from odoo import fields, models, api, _

class ResCompany(models.Model):

    _inherit = "res.company"
    def _localization_use_documents(self):
        """ Venezuela localization use documents """
        self.ensure_one()
        return True if self.country_id == self.env.ref('base.va') else super()._localization_use_documents()