from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Comment status seçenekleri
comment_status = [
    ("pending", "Pending"),
    ("approved", "Approved")
]

class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=155)
    status = models.CharField(max_length=250, choices=comment_status, default="pending")

    def __str__(self):
        return self.user.username

# pre_save sinyali için örnek bir fonksiyon
@receiver(pre_save, sender=Comment)
def print_email(sender, instance, **kwargs):
    print(f"User email: {instance.user.email}")
