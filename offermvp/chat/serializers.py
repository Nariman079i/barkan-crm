from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault

from chat.models import Messages, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar', 'email', 'username')


class MessageSerializer(ModelSerializer):
    recipient = UserSerializer(many=False, read_only=True)
    sender = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Messages
        fields = ('message', 'id', 'recipient', 'sender')
