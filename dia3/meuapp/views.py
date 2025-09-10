import requests
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView, UpdateView, DeleteView
from .models import Endereco
from .forms import EnderecoForm

class CepFormView(FormView):
    template_name = "cep_form.html"
    form_class = EnderecoForm
    success_url = reverse_lazy("endereco_list")

    def form_valid(self, form):
        cep = form.cleaned_data["cep"].replace("-", "")
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        data = response.json()

        Endereco.objects.create(
            cep=cep,
            logradouro=data.get("logradouro", ""),
            bairro=data.get("bairro", ""),
            localidade=data.get("localidade", ""),
            uf=data.get("uf", ""),
        )
        return super().form_valid(form)

class EnderecoListView(ListView):
    model = Endereco
    template_name = "endereco_list.html"
    context_object_name = "enderecos"

class EnderecoDetailView(DetailView):
    model = Endereco
    template_name = "endereco_detail.html"

class EnderecoUpdateView(UpdateView):
    model = Endereco
    fields = ["cep", "logradouro", "bairro", "localidade", "uf"]
    template_name = "endereco_form.html"
    success_url = reverse_lazy("endereco_list")

class EnderecoDeleteView(DeleteView):
    model = Endereco
    template_name = "endereco_confirm_delete.html"
    success_url = reverse_lazy("endereco_list")
