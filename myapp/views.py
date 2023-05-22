from rest_framework import viewsets
from .logic import modeloCNN
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PacientSerializer, ImageSerializer, DoctorSerializer
from .models import Pacient, Image, Doctor

# Create your views here.
class DoctorView(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class PacientView(viewsets.ModelViewSet):
    serializer_class = PacientSerializer
    queryset = Pacient.objects.all()

class ImageView(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

@api_view(['POST'])
def predecir(request):
    try:
        imagen = request.data.get('image')
        resul = modeloCNN.modeloCNN.predecir_tumor(modeloCNN.modeloCNN, url_imagen=imagen)
        return Response({'resul': resul})
    except Exception as e:
        return Response({'resul': str(e)})