from django.urls import path
from .views import (
    CepFormView, EnderecoListView, EnderecoDetailView,
    EnderecoUpdateView, EnderecoDeleteView
)

urlpatterns = [
    path("", CepFormView.as_view(), name="cep_form"),
    path("lista/", EnderecoListView.as_view(), name="endereco_list"),
    path("<int:pk>/", EnderecoDetailView.as_view(), name="endereco_detail"),
    path("<int:pk>/editar/", EnderecoUpdateView.as_view(), name="endereco_update"),
    path("<int:pk>/deletar/", EnderecoDeleteView.as_view(), name="endereco_delete"),
]
