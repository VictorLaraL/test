from django.db import migrations, models
import django.db.models.deletion

def forwards_func(apps, schema_editor):
    type_device = apps.get_model("main", "TypeDevice")
    status_device = apps.get_model("main", "StatusDevice")

    # Create the only 3 options in this model
    type_device.objects.create(type_device="Celda")
    type_device.objects.create(type_device="Aerogenerador")
    type_device.objects.create(type_device="Turbina Hidroelectrica")

    # Create the only 2 options in this model
    status_device.objects.create(status_device="En Operacion")
    status_device.objects.create(status_device="En Mantenimiento")

def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]