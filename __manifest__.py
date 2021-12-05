# -*- coding: utf-8 -*-
{
    'name': "infocli",
    'summary': """
        Información de importtadores y exportadores""",
    'description': """
        Infocli es  ...
    """,
    'author': "Tonitells",
    'website': "http://www.antonicastells.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'installabe': True,
    'application' : True,
    'category': 'trading',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base','mail','base_location_geonames_import'],
    # always loaded
    'data': [
        'demo/adreca.xml' ,
        'demo/portbase.xml' ,
        'views/accountmove.xml' ,
        'views/views.xml',
        'views/dettari.xml',
        'views/settings.xml' ,
        'views/facauto.xml',
        'views/item.xml',
        'views/barcos.xml',
        'views/livel_articles.xml',
        'views/escala.xml',
        'views/distance.xml',
        'views/portbase.xml',
        'views/res_city_view.xml',
        'views/partida.xml',
        'views/tarif_partner_cntr.xml',
        'views/tipcon.xml',
        'views/tipvehic.xml',
        'views/vehicles.xml',
        'views/remolcs.xml',
        'views/company.xml',
        'views/load_css.xml',
        'views/partner.xml',
        'views/adreca.xml',
        'views/especial.xml',
        'views/product_template.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
        'reports/albaran.xml' ,
        'reports/reports.xml',
        'data/data.xml' ,
        'data/mail_seal_to_client.xml' ,
    ],
    'css': ['static/src/css/livel.css'],
 }
