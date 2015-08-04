from openerp import models, fields, api
class customer_custom(models.Model):
    _inherit = "res.partner"
    customer_ntn = fields.Char(string="Customer NTN")
    customer_cnic = fields.Char(string="Customer CNIC")
    supplier_ntn = fields.Char(string="Supplier NTN")
    supplier_cnic = fields.Char(string="Supplier CNIC")
    buyer_type = fields.Selection([('registered','Registered'), ('unregistered','Unregistered'),('bulk_unregistered','Bulk-Unregistered'),('retail_customer','Retail Consumers')],"Buyer Type")
    province = fields.Selection([('punjab','Punjab'), ('sindh','Sindh'),('balochistan','Balochistan'),('capital','Capital Territory'),('kpk','KPK')],"Province")
    
