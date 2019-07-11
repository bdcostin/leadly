from core.models import Lead
from core.serializers import LeadSerializer
from rest_framework import generics

# Create your views here.

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
