from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('cadastro/', views.criar_conta, name='criar_conta'),
    path('cadastro/', views.CriarConta.as_view(), name='criar_conta'),
    path('usuarios/<int:pk>/editar',
         views.EditarConta.as_view(), name='editar_conta'),
    path('usuarios/<int:pk>/delete/',
         views.DeletarUser.as_view(), name='deletar_conta'),

    path('login/', views.login_page, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('jogos/cadastrar_jogo/', views.CriarJogo.as_view(), name='cadastrar_jogo'),
    path('jogos/<int:pk>/', views.DetalheJogo.as_view(), name='detail_jogo'),
    path('jogos/<int:pk>/editar/', views.EditarJogo.as_view(), name='editar_jogo'),
    path('jogos/<int:pk>/delete/',
         views.DeletarJogo.as_view(), name='deletar_jogo'),
]
