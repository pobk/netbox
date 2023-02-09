# Generated by Django 4.1.6 on 2023-02-09 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('extras', '0085_synced_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('data_path', models.CharField(blank=True, editable=False, max_length=1000)),
                ('data_synced', models.DateTimeField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('template_code', models.TextField()),
                ('environment_params', models.JSONField(blank=True, null=True)),
                ('data_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.datafile')),
                ('data_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.datasource')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
