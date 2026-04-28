from odoo import models, fields, api

class StudentRollUpdateWizard(models.TransientModel):
    _name = 'student.roll.update.wizard'
    _description = 'Update Student Roll Wizard'

    # current_roll এবং new_roll ইনপুট নেওয়ার জন্য
    new_roll = fields.Integer(string="New Roll Number", required=True)

    def action_update_roll(self):
        # active_id দিয়ে আমরা সেই স্টুডেন্টকে ধরব যার প্রোফাইল থেকে উইজার্ডটি ওপেন হয়েছে
        student_id = self.env.context.get('active_id')
        student_rec = self.env['student.model'].browse(student_id)
        
        if student_rec:
            student_rec.write({'roll': self.new_roll})
            
        print(f"Wizard: Roll updated to {self.new_roll} for {student_rec.name}")
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Success',
                'message': 'Roll Number Updated Successfully!',
                'type': 'success',
            }
        }