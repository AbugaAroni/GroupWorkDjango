from rest_framework import serializers
from .models import Business_centres,Profile,Neighbourhood

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username','location','user_avatar','neighbourhood')

class NeighbourhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighbourhood
        fields = ('name','centers')

class Business_centresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Business_centres
        fields = ('centre_name','contact_info','emergency_service')