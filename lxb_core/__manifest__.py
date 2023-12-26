# -*- coding: utf-8 -*-
{
    'name': "培训管理系统",

    'summary': """
        培训管理系统""",

    'description': """
        培训管理系统
    """,

    'author': "aibaifang",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'views/class_view.xml',
        'views/student_view.xml',
        'views/subject_menu_view.xml',
        'wizard/teacher_create_employee_wizard_view.xml',
        'data/sequence.xml',
        'views/teacher_view.xml',
        'security/ir.model.access.csv',
        'views/teacher_view.xml',
        'views/subject_view.xml',
    ],
    # only loaded in demonstration mode
   # 'demo': [
   #     'demo/demo.xml',
}
