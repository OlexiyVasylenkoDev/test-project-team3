from django.db import models

class DistributionCategory(models.Model):
    title = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class EmailDistribution(models.Model):
    category = models.ForeignKey(DistributionCategory, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=3000)

    def __str__(self):
        return f"{self.category} - {self.subject}"