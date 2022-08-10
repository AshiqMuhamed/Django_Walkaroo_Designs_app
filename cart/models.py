from django.db import models
from mensapp.models import tmens
from django.contrib.auth.models import User, auth

# Create your models here.
STATUS = (
    ('p1', 'Development Under P1'),
    ('p2', 'Development Under P2'),
    ('p3', 'Development Under P3'),
    ('p4', 'Development Under P4'),
    ('p5', 'Development Under P5'),
    ('reject', 'Rejected'),
    ('final', 'Finalised'))


class cartlist(models.Model):
    cproduct = models.ForeignKey(tmens, on_delete=models.CASCADE)
    cuser = models.ForeignKey(User, on_delete=models.CASCADE)
    ip = models.CharField(max_length=20, blank=True)
    added_at = models.DateField(auto_now_add=True)
    tilldate=models.IntegerField(default=0)
    status = models.CharField(max_length=100,choices=STATUS, default='p1')
    remarks = models.TextField(max_length=200, blank=True)


