from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_project_sample", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={},
        ),
        migrations.AddField(
            model_name="user",
            name="azure_id",
            field=models.UUIDField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="user",
            name="display_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="job_title",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
