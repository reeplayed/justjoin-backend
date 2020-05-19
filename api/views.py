from .serializers import OffertSerializer, LocationSerializer
from .models import Offert, Tech, Location
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        offerts = Location.objects.all()
        serializer = LocationSerializer(offerts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        
        try:
            location = Location.objects.get(place_id=data['place_id'])
        except Location.DoesNotExist:
            location = Location.objects.create(lat=data['lat'], lng=data['lng'], place_id = data['place_id'])

        offert_data = {
            'tech': data['tech'],
            'company_name': data['company_name'],
            'offer_title': data['offer_title'],
            'city': data['city'],
            'street': data['street'],
            'company_size': data['company_size'],
            'image': data['image'],
            'salary_from': data['salary_from'], 
            'salary_to': data['salary_to'], 
            'emp_type': data['emp_type'], 
            'exp_lvl': data['exp_lvl'],
            'place_id': data['place_id'],
            'location': location,
            'description': data['description']
        }

        offert = Offert(**offert_data)
        offert.save()

        for i in range(int(data['tech_size'])):
            tech_data = {
                'tech': data[f'tech_{i}'],
                'tech_lvl': int(data[f'tech_lvl_{i}']),
                'offert': offert
            }
            Tech.objects.create(**tech_data)
        
        print(offert)
       
        return Response({'mesaage':'Succes'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def detail_view(request, slug):
    try:
        offer = Offert.objects.get(slug=slug)
        serializer = OffertSerializer(offer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Offert.DoesNotExist:
        return Response({'message': "Offer does not exist.."}, status=401)