{
    "name": "Flight Data Sync",
    "version": "16.0.0.1",
    "author": "Apexive Solutions LLC",
    "website": "https://apexive.com",
    'license': "Other OSI approved licence",
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
        "static/description/icon.png",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
