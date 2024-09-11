from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class FlightFlight(models.Model):
    _inherit = 'flight.flight'

    event_time_ids = fields.One2many('flight.event.time', 'flight_id', string='Event Times',
                                     tracking=True,
                                     copy=True)
    phase_duration_ids = fields.One2many('flight.phase.duration', 'flight_id',
                                          compute='_compute_phase_durations', store=True,
                                          string='Phase Durations')

    @api.constrains('event_time_ids')
    def _check_event_sequence(self):
        for flight in self:
            latest_times = {}
            for event in flight.event_time_ids.sorted(
                    key=lambda r: r.code_id.sequence):
                if event.time_kind in latest_times and event.time < latest_times[
                    event.time_kind]:
                    raise ValidationError (_ (
                        "Invalid event sequence: %(event)s (%(time_kind)s) is out of order.",
                        event=event.code_id.name,
                        time_kind=event.time_kind
                    ))
                latest_times[event.time_kind] = event.time

    @api.depends('event_time_ids', 'event_time_ids.time', 'event_time_ids.code_id')
    def _compute_phase_durations(self):
        PhaseDuration = self.env['flight.phase.duration']
        Phase = self.env['flight.phase']

        for flight in self:
            phases = Phase.search([])
            durations = PhaseDuration.search([('flight_id', '=', flight.id)])
            durations.unlink ()  # Remove existing durations

            new_durations = []
            for phase in phases:
                start_event = flight.event_time_ids.filtered (
                    lambda
                        e: e.code_id == phase.start_event_code_id and e.time_kind == 'A'
                )
                end_event = flight.event_time_ids.filtered (
                    lambda
                        e: e.code_id == phase.end_event_code_id and e.time_kind == 'A'
                )

                if start_event and end_event and start_event.time and end_event.time:
                    duration = (
                                           end_event.time - start_event.time).total_seconds () / 3600.0
                    new_durations.append ({
                        'flight_id': flight.id,
                        'phase_id': phase.id,
                        'start_time': start_event.time,
                        'end_time': end_event.time,
                        'duration': round (duration, 2),
                    })

            flight.phase_duration_ids = [(0, 0, vals) for vals in new_durations]

    def _track_event_time_changes(self, event_time_vals):
        for record in self:
            changes = []
            for command in event_time_vals:
                if command[0] == 1:  # Update existing record
                    event_time_id = command[1]
                    new_values = command[2]
                    old_event_time = self.env['flight.event.time'].browse(event_time_id)

                    for field, new_value in new_values.items():
                        old_value = old_event_time[field]
                        if old_value != new_value:
                            changes.append(f"{old_event_time.display_name}: {field} changed from {old_value} to {new_value or 'None'}")

                elif command[0] == 0:  # Create new record
                    new_values = command[2]
                    changes.append(f"Added: {new_values}")

                elif command[0] == 2:  # Delete record
                    deleted_event_time = self.env['flight.event.time'].browse(command[1])
                    changes.append(f"Removed: {deleted_event_time.display_name}")

            if changes:
                message = "Event Times Updated:<br>" + "<br>".join(changes)
                record.message_post(body=message)

    def write(self, vals):
        if 'event_time_ids' in vals:
            self._track_event_time_changes(vals['event_time_ids'])
        return super(FlightFlight, self).write(vals)

