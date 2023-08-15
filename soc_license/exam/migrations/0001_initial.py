# Generated by Django 4.2.3 on 2023-08-15 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Answer",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("point", models.IntegerField(default=0)),
                ("count", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Level",
            fields=[
                (
                    "description",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "level",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exam.level"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QuestionText",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=500)),
                ("explanation", models.CharField(default="", max_length=500)),
                ("tips", models.CharField(default="", max_length=500)),
                (
                    "lang",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.lang"
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exam.question"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AnswerText",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=200)),
                (
                    "answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exam.answer"
                    ),
                ),
                (
                    "lang",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.lang"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="exam.question"
            ),
        ),
    ]
