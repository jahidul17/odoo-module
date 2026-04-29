from odoo import models,fields

class StudentRollUpdateWizard(models.TransientModel):
    _name='student.roll.update.wizard'
    _description='Update Student Roll Wizard'

    new_roll=fields.Integer(string="New Roll Number", required=True)

    def action_update_roll(self):
        student_id=self.env.context.get('active_id')
        student_rec=self.env['student.model'].browse(student_id)

        if student_rec:
            student_rec.write({'roll':self.new_roll})

        # print(f"Wizard: Roll update to {self.new_roll} for {student_rec.name}")

        return True



