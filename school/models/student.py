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

