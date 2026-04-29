{
    'name': 'School Management',
    'version': '19.0.1.0.0',
    'summary': 'School ERP management system',
    'sequence': 10,
    'description': """
        This module adds for student list view and kanban view.
    """,
    'category': 'Education',
    'author': 'Zahidul Islam', 
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/student_roll_update_view.xml',
        'views/student.xml',
        'views/menus.xml',
        

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}


