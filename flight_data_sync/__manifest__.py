{
    "name": "Flight Data Sync",
    "version": "16.0.0.1",
    "author": "Apexive Solutions LLC",
    "website": "https://github.com/smartops-aero/smartops-odoo-flight",
    'license': "LGPL-3",
    "category": "Industries",
    "summary": "Flight data synchronization from various providers",
    "depends": [
        "flight",
        "mail",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_cron_data.xml",
        "views/actions.xml",
        "views/flight_data_provider_views.xml",
        "views/menu.xml",
        "wizard/flight_data_sync_wizard_views.xml",
    ],
    "demo": [],
    "qweb": [],
    "images": [
        "static/description/banner.png",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
