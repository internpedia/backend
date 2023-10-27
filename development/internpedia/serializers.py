from rest_framework import serializers
from .models import Company, Internship, Review, Vote

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = '__all__'
        
    def to_representation(self, instance):
        instance.avgNumRating = round(float(instance.avgNumRating), 2)
        instance.site = instance.get_site_display()
        return super().to_representation(instance)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Vote 
        fields = '__all__'
