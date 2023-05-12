from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.models import AbstractUser
from django.db import models
from .admin import admin


# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/')


class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender',default=1)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient',default=1)
    message = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Send message to WebSocket
        # Получаем объект канала
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'chat_room_{self.recipient.pk}{self.sender.pk}',
            {
                'type': 'chat_message',
                'message': {'sender': self.recipient.email,
                            'message': self.message
                            }
            }
        )


admin.site.register(Messages)
admin.site.register(User)
