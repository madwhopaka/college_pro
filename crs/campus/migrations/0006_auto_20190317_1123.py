# Generated by Django 2.1.7 on 2019-03-17 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0005_comp_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_pos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(help_text='*required', max_length=30, unique=True)),
                ('username', models.CharField(help_text='*required', max_length=30)),
                ('company_name', models.CharField(help_text='*required', max_length=30)),
                ('designation', models.CharField(help_text='*required', max_length=30)),
                ('salary', models.IntegerField(help_text='*required')),
                ('bond_years', models.IntegerField(help_text='*required')),
                ('information_technology', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('mech', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('civil', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('eee', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('ece', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('chemical', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('cse', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='comp_details',
            name='type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stu_details',
            name='branch',
            field=models.CharField(choices=[('it', 'information_technology'), ('me', 'mech'), ('ce', 'civil'), ('eee', 'eee'), ('ece', 'ece'), ('ch', 'chemical'), ('cse', 'cse')], max_length=10),
        ),
    ]
