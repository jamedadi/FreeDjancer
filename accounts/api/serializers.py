from django.contrib.admin.utils import lookup_field
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from accounts.models import UserSkill, Portfolio
from jobs.models import Skill

User = get_user_model()


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ['id', 'title']


class UserSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()

    class Meta:
        model = UserSkill
        fields = ['id', 'skill', ]


class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = ['id', 'title', 'description', 'cover']


class UserRetrieveUpdateSerializer(serializers.ModelSerializer):
    skills = UserSkillSerializer(many=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'bids_left', 'avatar', 'has_kyc', 'skills',]
        read_only_fields = ['has_kyc', 'bids_left']


class UserReadOnlySerializer(serializers.ModelSerializer):
    skills = UserSkillSerializer(many=True)
    portfolios = PortfolioSerializer(many=True)
    follower_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'avatar', 'skills', 'portfolios', 'follower_count', 'following_count'
        ]

    def get_following_count(self, obj):
        return obj.followings.count()

    def get_follower_count(self, obj):
        return obj.followers.count()


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']

    def validate(self, attrs):
        validate_password(attrs.get('password'))
        if attrs.get('password') != attrs.get('password2'):
            raise ValidationError('error: passwords are not match')
        attrs.pop('password2')
        return attrs


class UserChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['old_password', 'password', 'password2']

    def validate(self, attrs):
        user = self.instance

        if not user.check_password(attrs.get('old_password')):
            raise ValidationError(_('entered wrong password'))
        if attrs.get('password') != attrs.get('password2'):
            raise ValidationError('error: passwords are not match')

        validate_password(attrs.get('password'))
        attrs.pop('password2')
        attrs.pop('old_password')
        return attrs

    def update(self, instance, validated_data):
        instance.password = make_password(validated_data.get('password'))
        instance.save()


