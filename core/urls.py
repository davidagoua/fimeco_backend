from django.urls import path
from core import views


urlpatterns = [
    path('districts/', views.DistrictListView.as_view(), name='districts'),
    path('circuits/', views.CircuitListView.as_view(), name='circuits'),
    path('eglises/', views.EgliseLocalListView.as_view(), name='eglises'),
    path('familles/', views.FamilleListView.as_view(), name='familles'),
    path('membres/', views.MemberListView.as_view(), name='membres'),
    path('souscriptions/', views.SouscriptionIndividuListView.as_view(), name='souscriptions'),
    path('paiements/', views.PaiementListView.as_view(), name='paiements')
]