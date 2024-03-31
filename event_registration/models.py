from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    entry_fee = models.DecimalField(max_digits=6, decimal_places=2)
    is_team_event = models.BooleanField(default=False)

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    whatsapp_number = models.CharField(max_length=15)
    team_members = models.JSONField(blank=True, null=True)  # Field to store team member names as a list

class Payment(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    screenshot = models.ImageField(upload_to='payment_screenshots/')
