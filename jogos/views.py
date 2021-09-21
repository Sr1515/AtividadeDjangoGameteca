from django.contrib.auth import get_user_model
from jogos.forms import JogoForm, UserCreateUpdate

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
user = get_user_model()


def index(request):
    if request.user.is_authenticated:
        jogos = models.Jogo.objects.all().filter(user=request.user)
        context = {
            'jogos': jogos
        }
        return render(request, 'jogos/index.html', context)
    else:
        return render(request, 'jogos/index.html')


def login_page(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'jogos/login.html', context={'form': form})


class CriarConta(CreateView):
    model = user
    form_class = UserCreateUpdate
    template_name = 'jogos/criar_conta.html'
    success_url = reverse_lazy('login')


class EditarConta(LoginRequiredMixin, UpdateView):
    model = user
    form_class = UserCreateUpdate
    template_name = 'jogos/editar_conta.html'
    success_url = reverse_lazy('index')

    login_url = '/login/'


class CriarJogo(LoginRequiredMixin, CreateView):
    model = models.Jogo
    form_class = JogoForm
    template_name = 'jogos/cadastrar_jogo.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditarJogo(LoginRequiredMixin, UpdateView):
    model = models.Jogo
    form_class = JogoForm
    template_name = 'jogos/editar_jogo.html'
    success_url = reverse_lazy('index')

    login_url = '/login/'


class DetalheJogo(LoginRequiredMixin, DetailView):
    model = models.Jogo
    template_name = 'jogos/listar.html'


class DeletarJogo(LoginRequiredMixin, DeleteView):
    model = models.Jogo
    success_url = reverse_lazy('index')
    template_name = 'jogos/confirmar_deletar.html'
    login_url = '/login/'


class DeletarUser(LoginRequiredMixin, DeleteView):
    model = user
    success_url = reverse_lazy('index')
    template_name = 'jogos/confirmar_deletar.html'
    login_url = '/login/'


class BuscarJogo(LoginRequiredMixin):
    pass
