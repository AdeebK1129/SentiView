from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'name',
            'age',
            'gender',
            'location',
            'created_at',
            'modified_at',
        ]
        read_only_fields = ['id', 'created_at', 'modified_at']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email', 
            'password', 
            'name', 
            'age', 
            'gender', 
            'location',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Create the user and set timestamps
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data.get('name'),
            age=validated_data.get('age'),
            gender=validated_data.get('gender'),
            location=validated_data.get('location'),
        )
        user.created_at = user.modified_at = user.created_at or user.modified_at
        user.save()
        return user
