from django.test import TestCase
from schedules.models import Schedule


class ScheduleModelTest(TestCase):

    def test_get_absolute_url(self):
        new_schedule = Schedule.objects.create()
        self.assertEqual(
            new_schedule.get_absolute_url(),
            '/schedules/{}'.format(new_schedule.id)
        )
