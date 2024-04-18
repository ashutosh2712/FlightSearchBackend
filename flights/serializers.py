from rest_framework.serializers import ModelSerializer
from flights.models import Flight

class FlightSerializer(ModelSerializer):
    
    class Meta :
        model = Flight
        fields = "__all__"
        
    