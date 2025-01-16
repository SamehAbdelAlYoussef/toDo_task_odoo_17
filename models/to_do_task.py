from odoo import models, fields
class Task(models.Model):
    _name = 'todo_task'
    # inherit tchater
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Task'
    name = fields.Char(tracking=1)
    name_id = fields.Many2one('res.partner', tracking=1,string='assign to')
    description = fields.Text(tracking=1)
    date_deadline = fields.Date(string='Deadline',tracking=1)
    states = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ],default='new',tracking=1)
    def action_button_in_progress(self):
        for rec in self:
            rec.states='in_progress'

    def action_button_in_new(self):
        for rec in self:
            rec.states='new'

    def action_button_in_completed(self):
        for rec in self:
            rec.states='completed'
