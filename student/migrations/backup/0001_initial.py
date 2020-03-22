# Generated by Django 2.1.3 on 2018-12-05 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import student.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(blank=True, max_length=255, null=True, verbose_name='street')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='city')),
                ('zip', models.IntegerField(blank=True, null=True, verbose_name='postal code')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe_name', models.CharField(blank=True, max_length=45, null=True, verbose_name='classe')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Classe',
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Parent_hasContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=255, null=True, verbose_name='contact')),
                ('type', models.IntegerField(choices=[(1, 'Mobile'), (2, 'Landline'), (3, 'Email'), (4, 'URL')], null=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parentcontact_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parentcontact_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "Parent's contact",
                'verbose_name_plural': "Parent's contacts",
            },
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=45, verbose_name='First name')),
                ('lname', models.CharField(max_length=45, verbose_name='Last name')),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive'), (2, 'Done'), (3, 'Cancelled')], default=1)),
                ('is_ICE', models.BooleanField(default=True)),
                ('bday', models.DateField(null=True, verbose_name='Birthday')),
                ('gender', models.IntegerField(choices=[(0, ''), (1, 'Male'), (2, 'Female')], default=0, null=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_address', to='student.Address')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Parent',
                'verbose_name_plural': 'Parents',
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.IntegerField(blank=True, choices=[(0, ''), (1, 'Mother'), (2, 'Father'), (3, 'Guardian'), (4, 'Grandmother'), (5, 'Grandfather'), (6, 'Uncle'), (7, 'Aunt')], default=0, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_membership', to='student.Parents')),
            ],
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(blank=True, max_length=45, null=True, verbose_name='Section')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('matricule', models.CharField(max_length=10, unique=True)),
                ('fname', models.CharField(max_length=45, verbose_name='First name')),
                ('lname', models.CharField(max_length=45, verbose_name='Last name')),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive'), (2, 'Graduated'), (3, 'Dismissed'), (4, 'Quit')], default=1)),
                ('bday', models.DateField(verbose_name='Birthday')),
                ('gender', models.IntegerField(choices=[(0, ''), (1, 'Male'), (2, 'Female')], default=0, null=True)),
                ('picture', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='%Y/Profile/', verbose_name='Picture', width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('start_date', models.DateField(auto_now=True, null=True)),
                ('end_date', models.DateField(default='1000-01-01', null=True)),
                ('ICE_details', models.TextField(blank=True, max_length=255, null=True)),
                ('comment', models.TextField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_address', to='student.Address')),
                ('classe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_classe', to='student.Classes')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_updated_by', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ManyToManyField(blank=True, related_name='student_parent', through='student.Relationship', to='student.Parents')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_section', to='student.Sections')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Student_hasContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=255, null=True, verbose_name='contact')),
                ('type', models.IntegerField(choices=[(1, 'Mobile'), (2, 'Landline'), (3, 'Email'), (4, 'URL')], null=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='studentcontact_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='studentcontact_updated_by', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_hascontact', to='student.Student')),
            ],
            options={
                'verbose_name': "Student's contact",
                'verbose_name_plural': "Student's contacts",
            },
        ),
        migrations.CreateModel(
            name='Student_hasDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('location', models.FileField(blank=True, null=True, upload_to=student.models.user_directory_path, verbose_name='Location')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='studentdoc_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='studentdoc_updated_by', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
            options={
                'verbose_name': "Student's document",
                'verbose_name_plural': "Student's documents",
            },
        ),
        migrations.AddField(
            model_name='relationship',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_membership', to='student.Student'),
        ),
        migrations.AddField(
            model_name='parent_hascontacts',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_hascontact', to='student.Parents'),
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together={('street', 'city')},
        ),
    ]
