from django.shortcuts import render
from rest_framework import viewsets, generics, views
from core import models
from core import serializers as core_serializers



class DistrictListView(generics.ListCreateAPIView):
    queryset = models.District.objects.all()
    serializer_class = core_serializers.DistrictSerializer


class CircuitListView(generics.ListCreateAPIView):
    queryset = models.Circuit.objects.all()
    serializer_class = core_serializers.CircuitSerializer


class EgliseLocalListView(generics.ListCreateAPIView):
    queryset = models.EgliseLocal.objects.all()
    serializer_class = core_serializers.EgliseLocalSerializer


class FamilleListView(generics.ListCreateAPIView):
    queryset = models.Famille.objects.all()
    serializer_class = core_serializers.FamilleSerializer


class MemberListView(generics.ListCreateAPIView):
    queryset = models.Membre.objects.all()
    serializer_class = core_serializers.MembreSerializer


class SouscriptionIndividuListView(generics.ListCreateAPIView):
    queryset = models.SouscriptionIndividu.objects.all()
    serializer_class = core_serializers.SouscriptionIndividuSerializer



class PaiementListView(generics.ListCreateAPIView):
    queryset = models.Paiement.objects.all()
    serializer_class = core_serializers.PaiementSerializer