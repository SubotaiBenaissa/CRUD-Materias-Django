from django.db import models
from django.db.models.enums import Choices

# Create your models here.

class Carrera(models.Model):

    codigo = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default = 5)

    class Meta:

        verbose_name = 'carrera'
        verbose_name_plural = 'carreras'

    def __str__(self):

        return self.nombre

class Estudiante(models.Model):

    id = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    fechaNacimiento = models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    class Meta:

        verbose_name = 'estudiante'
        verbose_name_plural = 'estudiantes'

    def __str__(self):
         
        texto = "{0}, {1}, {2}, {3}"

        if self.vigencia: 
            estadoEstudiante = "Vigente :D"        
        else: 
            estadoEstudiante = "No vigente D:"

        return texto.format(self.nombre, self.apellido, self.carrera, estadoEstudiante)

class Curso(models.Model):

    codigo = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=20)
    creditos = models.PositiveSmallIntegerField()
    profesor = models.CharField(max_length=50)

    class Meta: 

        verbose_name='curso'
        verbose_name_plural='cursos'

    def __str__(self):

        texto = "{0}, {1}, Docente: {2}"

        return texto.format(self.nombre, self.codigo, self.profesor)    

class Matricula(models.Model):

    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        texto = "{0} matriculad{1} en el curso {2}, fecha: {3}"

        if self.estudiante == "F":
            letraSexo = "a"
        else: 
            letraSexo = "o"

        return texto.format(self.estudiante, letraSexo, self.curso, self.fechaMatricula)  


