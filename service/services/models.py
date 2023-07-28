from django.core.validators import MaxValueValidator
from django.db import models

from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.PositiveIntegerField()

    def __str__(self):
        return f"Service: {self.name}"

class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount')
    )

    plan_type = models.CharField(choices=PLAN_TYPES, max_length=10)
    discount_persent = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
    def __str__(self):
        return f"Plan: {self.plan_type}"

class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='sunscriptions', on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='sunscriptions', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='sunscriptions', on_delete=models.PROTECT)

    def __str__(self):
        return f"Subscription: {self.client}"

