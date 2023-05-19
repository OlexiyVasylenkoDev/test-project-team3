from rest_framework import serializers
from distribution.models import DistributionCategory, EmailDistribution


class DistributionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DistributionCategory
        fields = ['title']

class EmailDistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDistribution
        fields = ['subject', 'message']
