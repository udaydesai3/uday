from odoo import models, fields,api,_
from odoo.exceptions import Warning ,UserError

class ProductEpt(models.Model):
    
    _name='product.ept'
    _description="Product EPT"
    #_inherit="product.template"
    #_order="date"
#    @api.depends('price', 'on_hand_quantity')
#    def _total_price(self):
#        for i in self:
#            i.total_price=i.price*i.on_hand_quantity
    
    @api.onchange('price','on_hand_quantity','type')
    def onchange_total_price(self):
        """
        func : this method is used for calculate total price.as well as check that constraints "Product Price should be minimum 100".
        param : no parameter
        return :no return
        """
        result={}
        product_category = self.env['product.category.ept']
        self.total_price=self.price * self.on_hand_quantity
        if self.price < 100:
            raise Warning('Product Price should be minimum 100')        
        result['domain'] = {'category_id':[('type','=',self.type)]}
        return result

        
    @api.model
    def create(self,vals):
        record=vals
        print(record)
        product = super(ProductEpt, self).create(vals)
        return product
    
    @api.multi
    def write(self,values):
        return super (ProductEpt,self).write(values)
    
    @api.multi
    def unlink(self):
        return super(ProductEpt,self).unlink()

    @api.multi
    def action_default_on_hand_quantity(self):
        """
        func:this method is used for to take default quantity and product name from form view and display on wizard
        param:
        return:
        """
        context = dict(self._context) or {}
        product_id = self.env['product.ept'].browse(self.id)
        context.update({'default_update_on_hand_quantity':product_id.on_hand_quantity,'default_product_wizard_id':product_id.id})

        #_wizard_view_id = self.env.ref('product_ept.product_quantity_wizard_form_view')

        return {
            'name': _('Update On Hand Quantity'),
            'type': 'ir.actions.act_window',
            'res_model': 'product.ept.wizard',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'context':  context,
            'views': [[self.env.ref('product_ept.product_quantity_wizard_form_view').id, 'form']]
        }

    @api.multi
    @api.depends('name', 'product_barcode')
    def name_get(self):
        res = []
        for record in self:
            name = record.name + ' [' + record.product_barcode + ']'
            res.append((record.id, name))
        return res

    @api.model
    def _name_search(self, name, args='None', operator='ilike', limit=50):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('name', operator, name), ('product_barcode', operator, name)]
        products = self._search(domain + args, limit=limit)
        return self.browse(products).name_get()

    def generate_excel_report(self):
        rec = self.browse()
        data = {}
        data['form'] = rec.read(['name', 'price', 'on_hand_quantity','total_price'])

        
    image1 = fields.Binary(string="Product Image",attachment=True)
    name = fields.Char(string="Product Name",help="Name",required="True")
    price = fields.Float(string="Price",help="Product Individual price",required="True")
    on_hand_quantity = fields.Integer(string="On Hand Quantity",help="Product Quantity",required="True")
    total_price = fields.Float(string='Total Price',help="Total Price")
    date = fields.Date(string="Date",help="Date")
    is_salable = fields.Boolean(string="Is Salable",help="Product is Salable or not")
    description = fields.Text(string="Description",help="Product Description")
    category_id = fields.Many2one('product.category.ept',string="Category")
    active = fields.Boolean(string="Active",help="Product is Active or not",default=True)
    brand_id = fields.Many2one('product.brand',string="Brand",help="Brand Name")
    product_barcode = fields.Char(string="Product Barcode",help="Product Barcode")
    product_brand = fields.Integer(string="No of Available Product",related='brand_id.no_available_product',help="No of Brand")
    
    reference_id = fields.Reference(string="Reference", selection=[('product.brand', 'Brand Name'),
                                                                 ('product.category.ept', 'Category Name')])
    type = fields.Selection([('stock able', 'Stock able'), ('service', 'Service'),('consumable','Consumable')],default="stock able", string='Type',help="Product Type")
    
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (product_barcode)',  'You can not give same product barcode !')
    ]
    
       