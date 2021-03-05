from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


# inheriting from a ModelSerializer, which automatically generates validators
#  for the serializer based on the model
class UserAccountSerializer(serializers.ModelSerializer):
    """
    Here I am  stating that the type of this attribute is required and should
     be unique amongst all User objects in our database.
    """
    first_name = serializers.CharField(max_length=32,
                                       validators=[UniqueValidator(queryset=User.objects.all())]
                                       )
    last_name = serializers.CharField(max_length=32,
                                      validators=[UniqueValidator(queryset=User.objects.all())]
                                      )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, min_length=8, max_length=15)

    class Meta:
        """
        This is stating that for our UserSerializer, the corresponding model is User
        and these are the fields that it contains.
        """
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "password")
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],
                                        email=validated_data['email'],
                                        password=validated_data['password'])
        if not validated_data['first_name']:
            raise ValueError("User firstname is required")
        if not validated_data['last_name']:
            raise ValueError("User lastname is required")
        if not validated_data['email']:
            raise ValueError("User must have an email address")
        if not validated_data['password']:
            raise ValueError("Password is required")
        elif len(validated_data['password']) < 8:
            raise ValueError("Password is too short")
        else:
            user.set_password(validated_data['password'])

        return user
