from django.db import models


class Telegram(models.Model):

    chat_id = models.CharField(max_length=100, verbose_name='чат id')
    is_active = models.BooleanField(default=False, verbose_name='статус')
