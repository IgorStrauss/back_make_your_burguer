from myb_app import models, serializers
from rest_framework import viewsets


class AdicionarPaesViewSet(viewsets.ModelViewSet):
    queryset = models.Paes.objects.all()
    serializer_class = serializers.PaesSerializer


class AdicionarCarneViewSet(viewsets.ModelViewSet):
    queryset = models.Carnes.objects.all()
    serializer_class = serializers.CarnesSerializer


class AdicionarOpcionalViewSet(viewsets.ModelViewSet):
    queryset = models.Opcionais.objects.all()
    serializer_class = serializers.OpcionaisSerializer


class AdicionarStatusBurguerViewSet(viewsets.ModelViewSet):
    queryset = models.Status_burguer.objects.all()
    serializer_class = serializers.Status_burguerSerializer


class AdicionarBurguerViewSet(viewsets.ModelViewSet):
    queryset = models.Burguers.objects.all()
    serializer_class = serializers.BurguersSerializer
