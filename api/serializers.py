from rest_framework import serializers
from .models import Offert, Tech, Location

class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tech
        fields = ['tech', 'tech_lvl']

class OffertSerializer(serializers.ModelSerializer):
    technology = TechSerializer(many=True)

    class Meta:
        model = Offert
        fields = '__all__'

class SlimOffertSerializer(serializers.ModelSerializer):
    technology = TechSerializer(many=True)

    class Meta:
        model = Offert
        fields = [  
                    'tech', 
                    'company_name',
                    'offer_title',
                    'city',
                    'street',
                    'salary_from',
                    'salary_to',
                    'place_id',
                    'exp_lvl',
                    'image',
                    'date_add',
                    'slug',
                    'technology'
                ]

class LocationSerializer(serializers.ModelSerializer):
    offerts = SlimOffertSerializer(many=True)

    class Meta:
        model = Location
        fields = '__all__'



