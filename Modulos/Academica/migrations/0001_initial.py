# Generated by Django 3.2 on 2021-10-26 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('codigo', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('duracion', models.PositiveSmallIntegerField(default=5)),
            ],
            options={
                'verbose_name': 'carrera',
                'verbose_name_plural': 'carreras',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('creditos', models.PositiveSmallIntegerField()),
                ('profesor', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'curso',
                'verbose_name_plural': 'cursos',
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=30)),
                ('fechaNacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('vigencia', models.BooleanField(default=True)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academica.carrera')),
            ],
            options={
                'verbose_name': 'estudiante',
                'verbose_name_plural': 'estudiantes',
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaMatricula', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academica.curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academica.estudiante')),
            ],
        ),
    ]
