# from odoo import models, fields, api

# class AccountAsset(models.Model):
#     _inherit='account.asset'

#     asset_product_ids=fields.Many2many('product.template',string="Asset Products",domain=[('is_asset','=',True)])
from odoo import models, fields, api

class AccountAsset(models.Model):
    _inherit = 'account.asset'

    name = fields.Char(string='Asset Name', required=False)
    
    asset_product_ids = fields.Many2many(
        'product.template', 
        string="Asset Products",
        domain=[('is_asset', '=', True)],
        required=True
    )

    @api.onchange('asset_product_ids')
    def _onchange_asset_products(self):
        if self.asset_product_ids:
            self.name = ", ".join(self.asset_product_ids.mapped('name'))