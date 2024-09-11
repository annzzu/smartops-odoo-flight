# Copyright 2024 Apexive <https://apexive.com/>
# License MIT (https://opensource.org/licenses/MIT).
from odoo import fields, models, api


class FlightPhaseDuration(models.Model):
    _name = 'flight.phase.duration'
    _description = 'Flight Phase Duration'

    name = fields.Char(compute='_compute_name', store=True)
    flight_id = fields.Many2one('flight.flight', string='Flight', readonly=True, ondelete='cascade')
    phase_id = fields.Many2one('flight.phase', string='Phase', readonly=True)
    start_time = fields.Datetime(string='Start Time', readonly=True)
    end_time = fields.Datetime(string='End Time', readonly=True)
    duration = fields.Float (string='Duration (hours)', compute='_compute_duration',
                             readonly=True)

    @api.depends('start_time', 'end_time')
    def _compute_duration(self):
        for record in self:
            if record.start_time and record.end_time:
                duration = (record.end_time - record.start_time).total_seconds () / 3600
                record.duration = round (duration, 2)
            else:
                record.duration = 0.0

    @api.depends('flight_id', 'phase_id', 'duration')
    def _compute_name(self):
        for record in self:
            record.name = f"{record.flight_id.id} - {record.phase_id.name}: {record.duration:.2f} hours"

    _sql_constraints = [
        ('unique_flight_phase', 'UNIQUE(flight_id, phase_id)', 'Each phase can only have one duration record per flight.')
    ]