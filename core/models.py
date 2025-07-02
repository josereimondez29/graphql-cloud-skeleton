import uuid
from django.db import models

class User(models.Model):
    PLAN_CHOICES = [
        ('HOBBY', 'Hobby'),
        ('PRO', 'Pro')
    ]

    id = models.CharField(primary_key=True, max_length=100, editable=False)
    username = models.CharField(max_length=150, unique=True)
    plan = models.CharField(max_length=10, choices=PLAN_CHOICES)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = f"u_{uuid.uuid4().hex[:8]}"
        super().save(*args, **kwargs)

class DeployedApp(models.Model):
    id = models.CharField(primary_key=True, max_length=100, editable=False)
    owner = models.ForeignKey(User, related_name='apps', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = f"app_{uuid.uuid4().hex[:8]}"
        super().save(*args, **kwargs)


# Create your models here.
