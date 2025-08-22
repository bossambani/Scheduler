from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="jobs")
    description = models.TextField()
    start_date = models.DateField()
    finish_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("in_progress", "In Progress"), ("completed", "Completed")],
        default="pending"
    )

    def __str__(self):
        return f"{self.description[:30]} ({self.client.name})"
