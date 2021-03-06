"""Serializers file."""
# Standard Library
from collections import OrderedDict

# Django
from django.contrib.auth import get_user_model

# 3rd-party
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

# Local
from .models import Company
from .models import CustomUser
from .models import StudentTeam

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer, RegisterSerializer):
    """User serializer."""

    account_type = serializers.ChoiceField(choices=CustomUser.ACCOUNT_TYPE)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    # company = serializers.SerializerMethodField()

    @staticmethod
    def modify_user(user, validated_data):  # noqa: D102
        user.account_type = validated_data['account_type']
        user.save()

    def save(self, request):  # noqa: D102
        user = super().save(request)
        self.modify_user(user, self.validated_data)
        return user

    class Meta:  # noqa: D106
        model = UserModel
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            'account_type',
            # 'average',
            # 'account_notes',
            # 'company',
        ]


class ClassicUserSerializer(serializers.ModelSerializer):
    """Grouped user serializer."""

    class Meta:  # noqa: D106
        model = UserModel
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'username',
            'average',
        ]


class CompanySerializer(serializers.ModelSerializer):
    """Company serializer."""

    def to_representation(self, instance):
        """Override serializer data generation."""
        data = super().to_representation(instance)
        students = UserSerializer(instance.customuser_set.all(), many=True)
        return OrderedDict([(data['name'], students.data)])

    class Meta:  # noqa: D106
        model = Company
        fields = [
            'name',
        ]


class GroupedCompanySerializer(serializers.ModelSerializer):
    """Grouped company serializer."""

    def to_representation(self, instance):
        """Override serializer data generation."""
        data = super().to_representation(instance)
        students = ClassicUserSerializer(
            instance.customuser_set.all(), many=True)
        return OrderedDict([(data['name'], students.data)])

    class Meta:  # noqa: D106
        model = Company
        fields = [
            'name',
        ]


class StudentTeamSerializer(serializers.ModelSerializer):
    """Student team serializer."""

    def to_representation(self, instance):
        """Override serializer data generation."""
        data = super().to_representation(instance)
        users = UserSerializer(instance.customuser_set.all(), many=True)
        return OrderedDict([(data['name'], users.data)])

    class Meta:  # noqa: D106
        model = StudentTeam
        fields = [
            'name',
        ]


class AssignStudentSerializer(serializers.Serializer):
    """Assign student serializer."""

    student = PrimaryKeyRelatedField(
        queryset=UserModel.objects.filter(account_type=CustomUser.STUDENT))
    company = PrimaryKeyRelatedField(
        queryset=Company.objects.all())

    def create(self, validated_data):  # noqa: D102
        pass

    def update(self, instance, validated_data):  # noqa: D102
        pass


class JustEmailSerializer(serializers.Serializer):
    """Just email serializer."""

    email = serializers.EmailField(required=False)

    def create(self, validated_data):  # noqa: D102
        pass

    def update(self, instance, validated_data):  # noqa: D102
        pass
