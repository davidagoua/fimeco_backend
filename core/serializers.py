from rest_framework import serializers
from core import models


class ChefFamilleRegisterSerializer(serializers.ModelSerializer):
    nom_famille = serializers.CharField()

    class Meta:
        model = models.Membre
        fields = ['nom','prenoms','date_naissance','lieu_naissance','occupation','egliseLocal']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = '__all__'


class CircuitSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField()

    class Meta:
        model = models.Circuit
        fields = '__all__'


class EgliseLocalSerializer(serializers.ModelSerializer):
    circuit = serializers.StringRelatedField()

    class Meta:
        model = models.EgliseLocal
        fields = '__all__'


class FamilleSerializer(serializers.ModelSerializer):
    eglise_local_id = serializers.IntegerField(write_only=True)
    eglise_local = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = models.Famille
        fields = '__all__'


class MembreSerializer(serializers.ModelSerializer):
    famille = FamilleSerializer(read_only=True)
    famille_id = serializers.IntegerField(write_only=True)
    eglise_local = serializers.StringRelatedField(read_only=True)
    eglise_local_id = serializers.IntegerField(write_only=True)


    class Meta:
        model = models.Membre
        fields = '__all__'



class SouscriptionIndividuSerializer(serializers.ModelSerializer):
    membre_id = serializers.IntegerField(write_only=True)
    membre = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.SouscriptionIndividu
        fields = '__all__'


class PaiementSerializer(serializers.ModelSerializer):
    famille_id = serializers.IntegerField(write_only=True)
    membre_id = serializers.IntegerField(write_only=True)
    membre = serializers.StringRelatedField(read_only=True)
    famille = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = models.Paiement
        fields = '__all__'

