from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Occurrence


class OccurrenceSerializer(serializers.ModelSerializer):
    """
    Occurrence Serializer
    - It shows all the fields in the Occurrence
    """

    class Meta:
        model = Occurrence
        fields = ['description', 'lat', 'lon', 'distance_from_hq', 'created_at',
                  'updated_at', 'status', 'category', 'author']


class UserSerializer(serializers.HyperlinkedModelSerializer):

    password = serializers.CharField(write_only=True)
    occurrences = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Occurrence.objects.all())

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password', 'occurrences')

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user
