from  rest_framework import serializers
from bt.models import Worm

class WormSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Worm
        depth = 2