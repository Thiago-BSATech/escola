from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

    
    def validate(self, dados):
        if len(dados['cpf']) != 11:
            raise serializers.ValidationError("O CPF deve conter exatamente 11 dígitos.")
        
        if len(dados['celular']) != 13:
            raise serializers.ValidationError("O numero de celular deve conter exatamente 13 dígitos.")
        
        if not dados['name'].isalpha():
                raise serializers.ValidationError('O nome só deve ter letras')
        

        return dados
    


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
    
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):

    cursos = serializers.ReadOnlyField(source = 'curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):

    estudante_name = serializers.ReadOnlyField(source = 'estudante.nome')

    class Meta:
        model = Matricula
        fields = ['estudante_name']