{
    'name': 'Legion Mobile Theme',
    'version': '15.0.1.0.1',
    'summary': 'Legion Mobile Theme',
    'author': 'Bytelegion',
    'license': 'AGPL-3',
    'maintainer': 'Bytelegion',
    'company': 'Bytelegion',
    'website': 'https://bytelegions.com',
    'depends': [
        'web'
    ],
    'category':'Branding',
    'description': """
           Legion Mobile Theme
    """,
    'assets': {
        'web._assets_primary_variables': [
            '/legion_mobile_theme/static/src/scss/primary_variables_custom.scss',
        ],
        'web._assets_secondary_variablesweb.assets_backend': [
            '/legion_mobile_theme/static/src/scss/fields_extra_custom.scss',
        ],
        'web._assets_secondary_variables': [
            '/legion_mobile_theme/static/src/scss/secondary_variables.scss',
        ],
    },
    'price':0,
    'currency':'USD',
    'installable': True,
    'auto_install': False,
    'application': True,
    'images': ['static/description/icon.png','static/description/main_screenshot.png']
}
