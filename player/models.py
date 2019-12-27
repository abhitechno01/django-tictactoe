from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Invitation(models.Model):
    from_user = models.ForeignKey(
        User, related_name="invitation_sent", on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name="invitation_received", on_delete=models.CASCADE)
    message = models.CharField(max_length=300)
    timestamp = models.DateField(auto_now_add=True)
