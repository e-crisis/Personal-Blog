# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class About(models.Model):
    body_text = models.TextField()


class Entry(models.Model):
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()

    def __str__(self):
        return self.headline


class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    comment_text = models.TextField()
    pub_date = models.DateField()


