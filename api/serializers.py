from rest_framework import serializers

from .models import Heros


class HerosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Heros
        fields = ('id','name', 'alias')