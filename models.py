import os
from django.db import models

class Visitor(models.Model):
    visitor_name = models.CharField(max_length=100, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    person_to_meet = models.CharField(max_length=100, blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
    photo_path = models.CharField(max_length=255, blank=True, null=True) # Changed to CharField for storing file path

    