from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import base64, time

class Student(models.Model):
    _name="student.model"
    _description="Student Model"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    

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

    name=fields.Char(string="Name", tracking=True)
    photo=fields.Image(string='Student Photo',max_width=1920,max_height=1920,verify_resolution=False)
    gender=fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ],string='Gender', default="male", tracking=True)

    birth_day=fields.Date(string="Date of Birth")
    division=fields.Selection('_get_division_list')

    @api.model
    def _get_division_list(self):
        return [('dhaka','Dhaka'),
                ('barisal','Barisal'),
                ('khulna','Khulna')]
    
    address=fields.Text(string='Address')
    about_html=fields.Html(string='Description',
        sanitize=True,
        strip_style=False,
        translate=True)
    
    joining_date=fields.Date("Date",default=fields.Date.context_today)
    start_date=fields.Date(default=time.strftime("%Y-01-01"))
    end_date=fields.Date(default=time.strftime("%Y-12-31"))

    # @api.constrains('joining_date')
    # def _chaeck_friday(self):
    #     for record in self:
    #         if record.joining_date:
    #             if record.joining_date.weekday()==4:
    #                 raise ValidationError("Friday is off day!")
    
    # additional_info=fields.Json(string="Extra Data")
    # def set_json_data(self):
    #     for record in self:
    #         record.additional_info={
    #             "blood_group":"A+",
    #             "hobby": "Coding",
    #             "emergency_contact": "123456789"
    #         }
    
    team_member_ids=fields.Many2many('student.model','student_tema_rel','student_id','member_id',string="Team Members")
    classmate_count = fields.Integer(compute='_compute_classmate_count', string="Classmates")

 #------------------------Status Bar add-------------------------------------
    state = fields.Selection([
        ('draft', 'Draft'),
        ('enrolled', 'Enrolled'),
        ('on_hold', 'On Hold'),
        ('suspended', 'Suspended'),
        ('graduated', 'Graduated'),
    ], string="Status", default='draft', tracking=True)

    def action_enroll(self):
        self.state = 'enrolled'

    def action_graduate(self):
        self.state = 'graduated'
    
    def action_suspend(self):
        for record in self:
            record.state = 'suspended'
    
    def action_on_hold(self):
        self.state = 'on_hold'
 
 
 #------------------------Smart button add-------------------------------------

    def _compute_classmate_count(self):
        for record in self:
            count = self.env['student.model'].search_count([
                ('gender', '=', record.gender),
                ('id', '!=', record.id)
            ])
            record.classmate_count = count

    def action_view_classmates(self):
        return {
            'name': _('Classmates'),
            'type': 'ir.actions.act_window',
            'res_model': 'student.model',
            'view_mode': 'list,form',
            'domain': [('gender', '=', self.gender), ('id', '!=', self.id)],
            'context': {'default_gender': self.gender},
            'target': 'current',
        }


#------------------------Explore ORM and .env Operations-------------------------------------

    # def explore_orm_operations(self):
    #     print("\n"+"="*30)
    #     print(" ORM operations start")
    #     print("="*30)

    #     find_roll=5
    #     create_test_roll=110
    #     updated_name='Yousuf Ali'
    #     copied_roll=120

    #     students=self.env['student.model'].search([('roll','=',find_roll)])
    #     if students:
    #         print(f"Search : Found student name is {students[0].name}")
    #     else:
    #         print("Search: No student found with roll")

    #     old_test_data=self.env['student.model'].search([('roll','=', create_test_roll)])
    #     if old_test_data:
    #         old_test_data.unlink()
    #         print("Old test data Roll  deleted to avoid error.")
    #     else:
    #         print('Does not exist so dont warry!')

    #     new_student=self.env['student.model'].create({
    #         'name':'Hanjala',
    #         'roll':create_test_roll,
    #         'gender':'male',
    #         'address':'Dhaka'
    #     })
    #     print(f"Create: New student created with ID: {new_student.id}")
    #     #Browsec always find id from database.
    #     browsed_rec=self.env['student.model'].browse(new_student.id)
    #     print(f"Browse: Fetched name via Browse: {browsed_rec.name}")

    #     browsed_rec.write({'name':updated_name})
    #     print(f'Write: Name Updated to: {browsed_rec.name}')

    #     copied_rec=browsed_rec.copy({'roll':copied_roll})
    #     print(f'Copy: Record duplicated with rolll: {copied_rec.roll}')

    #     copied_rec.unlink()
    #     print("Unlink: Copied record delete successfully.")

    #     print('===================Ok======================')
    #     print('=================Thanks====================')
    


#------------------------Explore search and filter method Operations-------------------------------------

    # def explore_orm_operations(self):
    #     print("\n" + "="*40)
    #     print("      SEARCH METHOD EXPLORATION")
    #     print("="*40)

    #     domain = [('roll', '>', 10), ('gender', '=', 'male')]
    #     students = self.env['student.model'].search(domain)
    #     print(f"1. Total Male students (Roll > 10): {len(students)}")

    #     z_students = self.env['student.model'].search([('name', '=ilike', 'Z%')], order='roll desc')
    #     print("2. Students starting with Z (Sorted by Roll):")
    #     for s in z_students:
    #         print(f"   - Name: {s.name}, Roll: {s.roll}")

    #     limited_students = self.env['student.model'].search([], limit=2)
    #     print(f"3. First two students in DB: {limited_students.mapped('name')}")

    #     total_count = self.env['student.model'].search_count([])
    #     print(f"4. Total students in system: {total_count}")

    #     print("="*40 + "\n")

    #     return {
    #         'type': 'ir.actions.client',
    #         'tag': 'display_notification',
    #         'params': {
    #             'title': 'Search Successful',
    #             'message': 'Check Terminal for detailed output!',
    #             'type': 'success',
    #         }
    #     }



