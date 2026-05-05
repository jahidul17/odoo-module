{
    'name': 'Recruiter Approval Management',
    'version': '19.0.1.0.0',
    'summary': 'Multi-level approval process for Job Posts (PM -> HR -> CEO)',
    'sequence': 10,
    'description': """
        This module adds a custom status flow for hr.job:
        1. Draft
        2. PM Approved (triggers email to HR)
        3. HR Approved (triggers email to CEO)
        4. Published (Approved by CEO)
    """,
    'category': 'Education',
    'author': 'Zahidul Islam', 
    'license': 'LGPL-3',
    'depends': ['base', 'hr_recruitment','website_hr_recruitment','mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/stage.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}