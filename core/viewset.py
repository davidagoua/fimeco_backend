from rest_framework.viewsets import generics, ModelViewSet
from rest_framework import serializers, views
from .models import EgliseLocal



class EgliseLocalSerializer(serializers.ModelSerializer):

    class Meta:
        model= EgliseLocal
        fields = ['nom']


class EgliseLocalListView(ModelViewSet):
    model = EgliseLocal
    serializer_class = EgliseLocalSerializer
    queryset = EgliseLocal.objects.all()

    def get_queryset(self):
        return EgliseLocal.objects.all()
    

class FamilleInscriptionView(views.APIView):
    pass