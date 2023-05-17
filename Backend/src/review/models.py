from django.db import models

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Terrible'),
        (2, '2 - Bad'),
        (3, '3 - Okay'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]

    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    title = models.CharField(max_length=200)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.title}" for "{self.product.title}" by {self.user.email}'