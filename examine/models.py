# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.from django.conf import settings

class Dictionary(models.Model):
    Engsub = models.TextField(max_length=20)
    Vietsub = models.TextField(max_length=200)
