# Generated by Django 3.2.9 on 2021-11-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Sure',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'pub_date',
                    models.DateTimeField(verbose_name='date published'),
                ),
                (
                    'q01',
                    models.IntegerField(
                        choices=[
                            (4, 'Nunca'),
                            (3, 'Em 1 Ou 2 Dias'),
                            (2, 'Em 3 Ou 4 Dias'),
                            (1, 'Em 5 Ou 6 Dias'),
                            (0, 'Todos Os Dias'),
                        ]
                    ),
                ),
                (
                    'q02',
                    models.IntegerField(
                        choices=[
                            (4, 'Nunca'),
                            (3, 'Em 1 Ou 2 Dias'),
                            (2, 'Em 3 Ou 4 Dias'),
                            (1, 'Em 5 Ou 6 Dias'),
                            (0, 'Todos Os Dias'),
                        ]
                    ),
                ),
                (
                    'q03',
                    models.IntegerField(
                        choices=[
                            (4, 'Nunca'),
                            (3, 'Em 1 Ou 2 Dias'),
                            (2, 'Em 3 Ou 4 Dias'),
                            (1, 'Em 5 Ou 6 Dias'),
                            (0, 'Todos Os Dias'),
                        ]
                    ),
                ),
                (
                    'q04',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q05',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q06',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q07',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q08',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q09',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q10',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q11',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q12',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q13',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q14',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q15',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q16',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q17',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q18',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q19',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q20',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q21',
                    models.IntegerField(
                        choices=[
                            (4, 'Todo O Tempo'),
                            (3, 'A Maior Parte Do Tempo'),
                            (2, 'Boa Parte Do Tempo'),
                            (1, 'Uma Pequena Parte Do Tempo'),
                            (0, 'Em Nenhum Momento'),
                        ]
                    ),
                ),
                (
                    'q22',
                    models.IntegerField(
                        choices=[
                            (4, 'Não Importante'),
                            (3, 'Pouco Importante'),
                            (2, 'Importante'),
                            (1, 'Muito Importante'),
                        ]
                    ),
                ),
                (
                    'q23',
                    models.IntegerField(
                        choices=[
                            (4, 'Não Importante'),
                            (3, 'Pouco Importante'),
                            (2, 'Importante'),
                            (1, 'Muito Importante'),
                        ]
                    ),
                ),
                (
                    'q24',
                    models.IntegerField(
                        choices=[
                            (4, 'Não Importante'),
                            (3, 'Pouco Importante'),
                            (2, 'Importante'),
                            (1, 'Muito Importante'),
                        ]
                    ),
                ),
                (
                    'q25',
                    models.IntegerField(
                        choices=[
                            (4, 'Não Importante'),
                            (3, 'Pouco Importante'),
                            (2, 'Importante'),
                            (1, 'Muito Importante'),
                        ]
                    ),
                ),
                (
                    'q26',
                    models.IntegerField(
                        choices=[
                            (4, 'Não Importante'),
                            (3, 'Pouco Importante'),
                            (2, 'Importante'),
                            (1, 'Muito Importante'),
                        ]
                    ),
                ),
            ],
        ),
    ]
