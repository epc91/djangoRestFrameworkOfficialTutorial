from django.contrib.auth.models import User, Group
from django.db.models import fields
from rest_framework import serializers

# Use hyperlinking is good RESTful design
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
    
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']