import datetime

from django.db import models


class OnCall (models.Model):
    rule = models.TextField(
        verbose_name='on-call rule',
        help_text='Python statement for determining the on-call admin')

    def get_on_call(self, now=None):
        if now is None:
            now = datetime.datetime.now()
        exec(self.rule)
