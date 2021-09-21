from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
# from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Genero(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Plataforma(models.Model):
    titulo = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo


class Endereco(models.Model):
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)


class Desenvolvedor(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Jogo(models.Model):

    CHOICES = (
        (0, 'Ruim'),
        (1, 'Bom'),
        (2, 'Muito bom'),
        (3, 'Ótimo')
    )

    nome = models.CharField(max_length=255)
    lancamento = models.DateField()
    generos = models.ManyToManyField(Genero, related_name='jogos')
    plataformas = models.ManyToManyField(Plataforma, related_name='jogos')
    avaliacao = models.IntegerField(choices=CHOICES, null=True, blank=True)
    capa = models.ImageField(upload_to='pictures/%Y/%m/', blank=True)
    desenvolvedor = models.ForeignKey(
        Desenvolvedor, on_delete=models.DO_NOTHING, null=True, blank=True)
    enredo = models.TextField(max_length=500)
    critica = models.TextField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    @property
    def get_avaliacao(self):
        if self.avaliacao == 0:
            return "Ruim"
        elif self.avaliacao == 1:
            return "Bom"
        elif self.avaliacao == 2:
            return "Muito bom"
        else:
            return "Ótimo"
