from rest_framework import serializers
from crawlthesite.models import SanctionsList


class SanctionsListSerializer(serializers.ModelSerializer):

     class Meta:
         model = SanctionsList
         fields = '__all__'