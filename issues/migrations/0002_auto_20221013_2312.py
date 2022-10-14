from django.db import migrations

def populate_status(apps, schemaeditor):
    statuses = {
        "TO DO": "An issue that has not been started yet",
        "IN PROGRESS": "An issue that is actively being worked on",
        "DONE": "An issue that has successfully been completed",
    }
    Status = apps.get_model("issues", "Status")
    for key, desc in statuses.items():
        status_obj = Status(name=key, description=desc)
        status_obj.save()

def populate_impact(apps, schemaeditor):
    impacts = {
        "CRITICAL": "The measure of high effect (positive or negative) of an issue",
        "SIGNIFICANT": "The measure of medium effect (positive or negative) of an issue",
        "MINOR": "The measure of low effect (positive or negative) of an issue",
    }
    Impact = apps.get_model("issues", "Impact")
    for key, desc in impacts.items():
        impact_obj = Impact(name=key, description=desc)
        impact_obj.save()

def populate_urgency(apps, schemaeditor):
    urgencies = {
        "HIGH": "The measure of shortest due date of an issue",
        "MEDIUM": "The measure of medium due date of an issue",
        "LOW": "The measure of longest due date of an issue",
    }
    Urgency = apps.get_model("issues", "Urgency")
    for key, desc in urgencies.items():
        urgency_obj = Urgency(name=key, description=desc)
        urgency_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ("issues", "0001_initial"),
    ]

    operations = [migrations.RunPython(populate_impact),
                migrations.RunPython(populate_urgency), 
                migrations.RunPython(populate_status)
    ]