# Generated by Django 2.1.5 on 2019-12-21 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offset', models.CharField(max_length=1024)),
                ('is_checked', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'annotation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('project_id', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'label_document',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('shortcut', models.CharField(max_length=8)),
                ('background_color', models.CharField(max_length=8)),
                ('text_color', models.CharField(max_length=8)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'label_label',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'label_project',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='label',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_label', to='label.Project'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='document_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_annotation', to='label.Document'),
        ),
    ]
