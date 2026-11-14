{
    "name": "Tienda UNICAH",
    "version": "20.0.1.0.0",
    "summary": "Convenios de descuento para la tienda universitaria",
    "category": "Sales/Sales",
    "author": "José Fúnez",
    "depends": ["sale_management"],
    "data": [
        "security/ir.access.csv",
        "data/tienda_convenio_data.xml",
        "views/res_partner_views.xml",
        "views/tienda_convenio_views.xml",
        "views/sale_order_views.xml",
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
