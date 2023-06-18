from rest_framework import serializers
from Users.models import UserDetails

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('id', 
        'firstName', 
        'lastName',
        'email',
        'place',
        'age',
        'occupation',
        'describeYourself'

        
        )