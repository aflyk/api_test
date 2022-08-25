from rest_framework import serializers
from .models import Phones


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = ['phone', 'entity_id', 'snils',
                  'oiv_id', 'theme_id', 'request_id']

