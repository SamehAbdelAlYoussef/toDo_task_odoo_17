from odoo import models, fields,api
class Task(models.Model):
    _name = 'todo_task'
    # inherit tchater
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Task'
    name = fields.Char(tracking=1)
    name_id = fields.Many2one('res.partner', tracking=1,string='assign to')
    description = fields.Text(tracking=1)
    active = fields.Boolean(default=True)
    is_late = fields.Boolean(default=False)
    totalTime=fields.Integer(string='Total Time',compute='_compute_total_time',store=True)
    date_deadline = fields.Date(string='Deadline',tracking=1)
    estimated_time_ids=fields.One2many('all_task','all_task_id')
    states = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed'),
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

    def action_closed_server(self):
        for rec in self:
            rec.states='closed'

    # def check_date_deadline(self):
    #     tasks_ids = self.search([])
    #     for rec in tasks_ids:
    #         if rec.date_deadline and rec.date_deadline < fields.Date.today():
    #             rec.is_critical=True

    def check_expected_selling_date(self):
        task_ids = self.search([])
        for rec in task_ids:
            if rec.date_deadline and rec.date_deadline < fields.Date.today():
                rec.is_late = True

    @api.depends('estimated_time_ids.time')
    def _compute_total_time(self):
        for rec in self:
            rec.totalTime = sum(line.time for line in rec.estimated_time_ids)

class Time(models.Model):
    _name = 'all_task'
    _description = 'AllTask'

    rel_time=fields.Date('real time')
    time=fields.Integer('time')
    description=fields.Text('description')
    all_task_id=fields.Many2one('todo_task')
