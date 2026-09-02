# -*- coding: utf-8 -*-

{
    'name': 'Reporte ISN',
    'summary': '',
    'description': '''Cambios en el reporte de ISN''',
    'author': 'IT Admin',
    'version': '17.02',
    'category': 'Employees',
    'depends': [
        'nomina_cfdi_ee',
        'report_xlsx', 'om_hr_payroll',
    ],
    'data': [
        'views/hr_salary_view.xml',
    ],
    'assets': {
    },
    'installable': True,
    'application': False,
    'license': 'AGPL-3',
}
