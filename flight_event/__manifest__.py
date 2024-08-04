# -*- coding: utf-8 -*-
{
    'name': "Flight Events",

    'summary': """
        A technical module for tracking flight events and phases.""",

    'description': """
        This module extends the base Flight module to provide tracking of flight events and phases, e.g. takeoff, landing, etc times
    """,

    'author': "Apexive Solutions LLC",
    'website': "https://apexive.com",
    'license': "Other OSI approved licence",
    'category': 'Industries',
    'version': '16.0.0.3',

    'depends': [
        'base',
        'flight',
    ],

    'assets': {
        'web.assets_backend': [
            'flight_event/static/src/components/relative_datetimepicker/relative_datetimepicker.js',
            'flight_event/static/src/scss/flight_event_time_matrix.scss',
            'flight_event/static/src/components/flight_event_time_matrix_field/flight_event_time_matrix_field.js',
            'flight_event/static/src/components/flight_event_time_matrix_renderer/flight_event_time_matrix_renderer.js',
            'flight_event/static/src/components/flight_event_time_matrix_field/flight_event_time_matrix_field.xml',
            'flight_event/static/src/components/flight_event_time_matrix_renderer/flight_event_time_matrix_renderer.xml',
        ],
    },

    'data': [
        'security/ir.model.access.csv',
        'views/flight_event_code_views.xml',
        'views/flight_event_time_views.xml',
        'views/flight_phase_views.xml',
        'views/flight_views.xml',
        'data/flight.event.code.csv',
        'data/flight.phase.csv',
        'views/menu.xml',
    ],

    'application': False,
    'installable': True,
    'auto_install': False,
}
