from django.db import models
from django.core.urlresolvers import reverse


class Schedule(models.Model):

    def get_absolute_url(self):
        return reverse('view_schedule', args=[self.id])
