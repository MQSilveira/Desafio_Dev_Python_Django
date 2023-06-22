# Generated by Django 4.2.2 on 2023-06-18 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCompleto', models.CharField(max_length=100, verbose_name='Nome Completo')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('endereco', models.CharField(max_length=200)),
                ('valorEmprestimoPretendido', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor do Emprestimo Pretendido')),
                ('situacao', models.CharField(default='Em Analise', max_length=10, verbose_name='Situação')),
            ],
            options={
                'db_table': 'tabela_proposta',
            },
        ),
    ]
