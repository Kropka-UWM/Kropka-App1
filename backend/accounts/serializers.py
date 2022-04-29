"""Serializers file."""
from django.contrib.auth import get_user_model
from rest_framework import serializers
from backend.accounts.models import CustomUser

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """User serializer."""

    account_type = serializers.ChoiceField(choices=CustomUser.ACCOUNT_TYPE)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):  # noqa: D102
        user = UserModel.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            password=validated_data['password'],
            account_type=validated_data['account_type'],
        )
        return user

    class Meta:
        model = UserModel
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'username',
            'password',
            'account_type',
        ]