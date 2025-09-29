from django.db import models
from django.core.validators import MinLengthValidator

class Estudante(models.Model):
    nome = models.CharField(max_length = 100, blank = False)
    email = models.EmailField(blank = False, max_length= 30)
    cpf = models.CharField(max_length=11, unique=True, blank = False)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length= 14)

    def __str__(self):
        return self.nome


class Curso(models.Model):

    NIVEL = {
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    }

    codigo = models.CharField(validators=[MinLengthValidator(2)], max_length = 10, blank = False, unique = True)
    descricao = models.CharField(max_length = 100)
    nivel = models.CharField(max_length = 1, blank = False, null = False, choices = NIVEL, default='B')
   

    def __str__(self):
        return self.codigo
    

class Matricula(models.Model):

    PERIODO = {
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
        ('R', 'Remoto'),
    }

    estudante = models.ForeignKey(Estudante, on_delete = models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    periodo = models.CharField(max_length = 3, blank = False, null=False, choices=PERIODO, default='M')