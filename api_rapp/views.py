from rest_framework import viewsets, generics
from .models import Phones
from .serializers import PhoneSerializer
import datetime
# Create your views here.


class PhoneAPIView(viewsets.ModelViewSet):
    queryset = Phones.objects.filter(
        id_dt__date=datetime.datetime.now().date())
    serializer_class = PhoneSerializer


class PhoneAllData(generics.ListAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhoneSerializer


