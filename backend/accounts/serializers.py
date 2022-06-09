"""Serializers file."""
# Standard Library
from collections import OrderedDict

# Django
from django.contrib.auth import get_user_model

# 3rd-party
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

# Local
from .models import Company
from .models import CustomUser
from .models import StudentTeam

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """User serializer."""

    account_type = serializers.ChoiceField(choices=CustomUser.ACCOUNT_TYPE)
    password = serializers.CharField(write_only=True)
    company = serializers.SerializerMethodField()

    @staticmethod
    def get_company(obj):  # noqa: D102
        if obj.company:
            return f'{obj.company.name}'

    def create(self, validated_data):  # noqa: D102
        user = UserModel.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            password=validated_data['password'],
            account_type=validated_data['account_type'],
            average=validated_data['average'],
            account_notes=validated_data['account_notes'],
        )
        return user

    class Meta:  # noqa: D106
        model = UserModel
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'username',
            'password',
            'account_type',
            'average',
            'account_notes',
            'company',
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
