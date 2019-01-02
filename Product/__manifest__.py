{

    'name':'Product Ept',
    'version':'1.0',
    'depends':['base','product_brand'],
    'summary': 'Product Ept Module',
    'description':'this module is used for maintaining products details you can create new product and view all products',
    'data': ['security/ir.model.access.csv','views/product_ept_views.xml','views/product_category_views.xml'
             
        
    ],
    'demo': [
        
    ],
  
    'installable': True,
    'application': True,
    'auto_install': False,
}