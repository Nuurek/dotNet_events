from django.test import TestCase
from schedules.models import Schedule


class HomePageTest(TestCase):

    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_new_schedule_button_rediects_to_new_schedule(self):
        response = self.client.post(
            '/schedules/new',
        )
        new_schedule = Schedule.objects.first()
        self.assertRedirects(response, '/schedules/{}'.format(new_schedule.id))


class ScheduleViewTest(TestCase):

    def test_uses_schedule_template(self):
        schedule = Schedule.objects.create()
        schedule_url = '/schedules/{}'.format(schedule.id)
        response = self.client.get(schedule_url)
        self.assertTemplateUsed(response, 'schedule.html')
