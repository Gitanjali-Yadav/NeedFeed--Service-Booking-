from django.db import models

class ServiceCategory(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    is_emergency = models.BooleanField(default=False)
    icon = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    base_price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.DurationField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.category})"