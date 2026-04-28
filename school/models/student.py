from odoo import fields, models, api,_
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name="student.model"
    _description="Student Model"

    roll=fields.Integer(string="Roll Number", copy=False)

    # _sql_constraints=[
    #     ('unique_roll','unique(roll)','This roll already used.')
    # ]

    @api.constrains('roll')
    def _check_unique_roll(self):
        for record in self:
            if record.roll <= 0:
                raise ValidationError(_("Roll number must be greater than 0."))    
            existing_student = self.search([('roll', '=', record.roll), ('id', '!=', record.id)])
            if existing_student:
                raise ValidationError(_("Roll No %s already exists!") % record.roll)

    name=fields.Char(string="Name")
    photo=fields.Image(string='Student Photo',max_width=1920,max_height=1920,verify_resolution=False)
    gender=fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ],string='Gender', default="male")
    birth_day=fields.Date(string="Date of Birth")
    address=fields.Text(string='Address')

    
    def explore_orm_operations(self):
        print("\n"+"="*30)
        print(" ORM operations start")
        print("="*30)

        find_roll=5
        create_test_roll=110
        updated_name='Yousuf Ali'
        copied_roll=120

        students=self.env['student.model'].search([('roll','=',find_roll)])
        if students:
            print(f"Search : Found student name is {students[0].name}")
        else:
            print("Search: No student found with roll")

        old_test_data=self.env['student.model'].search([('roll','=', create_test_roll)])
        if old_test_data:
            old_test_data.unlink()
            print("Old test data Roll  deleted to avoid error.")
        else:
            print('Does not exist so dont warry!')

        new_student=self.env['student.model'].create({
            'name':'Hanjala',
            'roll':create_test_roll,
            'gender':'male',
            'address':'Dhaka'
        })
        print(f"Create: New student created with ID: {new_student.id}")
        #Browsec always find id from database.
        browsed_rec=self.env['student.model'].browse(new_student.id)
        print(f"Browse: Fetched name via Browse: {browsed_rec.name}")

        browsed_rec.write({'name':updated_name})
        print(f'Write: Name Updated to: {browsed_rec.name}')

        copied_rec=browsed_rec.copy({'roll':copied_roll})
        print(f'Copy: Record duplicated with rolll: {copied_rec.roll}')

        copied_rec.unlink()
        print("Unlink: Copied record delete successfully.")

        print('===================Ok======================')
        print('=================Thanks====================')
    






