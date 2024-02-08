{
    'name': "Venezuela - Extension Localizacion ",
    'summary': """
        Agregados a la localizacion Republica Venezuela.
        Tipos de identificacion,
        Estados,
        Tipos de documentos contables.
        Impuestos,
        Zona Francas
    """,
    'description': """
        
    """,
    
    'author': 'Autodidactada IT - Fabian',
    'website': 'https://autodidactati.com/',
    'category': 'Localizacion',
    'version': "1.0",
    'depends': [
        'base',
        'l10n_ve',
        'l10n_latam_base',
        'l10n_latam_invoice_document',
        'web_domain_field',
        ],

    'data': [
        'data/l10n_latam_identification_type_extras.xml',
        'data/l10n_latam_document_type_extras.xml',
        'data/l10n_res_country_state_extras.xml',
        'data/l10n_account_tax.xml',
        'views/l10n_ve_res_country.xml',
        'views/l10n_ve_extras_res_partner.xml'
    ],

    'application': False,
    'installable': True,
    'license': 'LGPL-3',
}
