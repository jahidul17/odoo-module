from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class StudentChatter(models.Model):
    _inherit = "student.model"

    def write(self, vals):
        if 'photo' in vals:
            photo_data = vals.get('photo')
            for record in self:
                if photo_data:
                    attachment_value = {
                        'name': f"Photo of {record.name or 'Student'}",
                        'datas': photo_data,
                        'res_model': 'student.model',
                        'res_id': record.id,
                    }
                    attachment = self.env['ir.attachment'].create(attachment_value)
                    record.message_post(
                        body="A new photo has been uploaded and attached.",
                        # attachment_ids=[attachment.id]
                    )
                else:
                    record.message_post(body="The student photo has been removed.")
        return super(StudentChatter, self).write(vals)
    
