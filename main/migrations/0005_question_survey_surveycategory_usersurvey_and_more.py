# Generated by Django 4.0.6 on 2022-08-01 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210223_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('single', 'Можно выбрать один ответ'), ('multi', 'Можно выбрать много ответов')], max_length=6)),
                ('title', models.CharField(blank=True, max_length=300)),
                ('logo', models.ImageField(blank=True, upload_to='upload')),
                ('var1', models.CharField(blank=True, max_length=300)),
                ('var2', models.CharField(blank=True, max_length=300)),
                ('var3', models.CharField(blank=True, max_length=300)),
                ('var4', models.CharField(blank=True, max_length=300)),
                ('var5', models.CharField(blank=True, max_length=300)),
                ('var6', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('logo', models.ImageField(blank=True, upload_to='upload')),
                ('date', models.DateTimeField()),
                ('mini_description', models.CharField(blank=True, max_length=300)),
                ('description', models.TextField(blank=True, max_length=600)),
                ('rating', models.IntegerField(blank=True, default=0)),
                ('status', models.IntegerField(blank=True, default=0)),
                ('view', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('icon', models.CharField(blank=True, max_length=300)),
                ('status', models.IntegerField(blank=True, default=0)),
                ('rating', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('like', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
                ('survey_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.survey')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.AddField(
            model_name='usertestitem',
            name='questions',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='usertestitem',
            name='true_question',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='UserSurveyItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choosen_variant', models.CharField(max_length=300)),
                ('date', models.DateTimeField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.question')),
                ('user_survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.usersurvey')),
            ],
        ),
        migrations.AddField(
            model_name='survey',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.surveycategory'),
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.survey'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=1000)),
                ('date', models.DateTimeField(blank=True)),
                ('rating', models.FloatField(blank=True, default=0.0)),
                ('status', models.IntegerField(blank=True, default=0)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.survey')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
