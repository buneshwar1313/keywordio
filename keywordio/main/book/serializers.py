from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *
from rest_framework import  exceptions
from rest_framework.authtoken.models import Token


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True,write_only=True)
    password2 = serializers.CharField(required=True,write_only=True)

    class Meta:
        model = UserProfile
        fields = [
            'name',
            'email',
            'password',
            'password2',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def create(self, validated_data):
        email = validated_data.get('email')
        name = validated_data.get('name')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')
        if password == password2:
            user = UserProfile(email =email, name= name)
            user.save()
            return user
        else:
            raise serializers.ValidationError({
                'error':'both password do not ,match'
            })

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = UserProfile
        fields=[
            'email',
            'password',
        ]
    def validate(self,data):
        email = data.get("email","")
        password = data.get("password","")
        if email and password:
            user =authenticate(email =email, password=password)
            if user:

                data['user']=user


            else:
                msg = "unable to login Username or Password is wrong"
                raise exceptions.ValidationError(msg)
        else:
            msg = "must provide username and password both"
            raise exceptions.ValidationError()
        return data


class BookSerializers(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'