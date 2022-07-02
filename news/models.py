from django.db import models

# Create your models here.


class News(models.Model):
    name = models.CharField("Text Title,", max_length=200)
    text = models.TextField("Text Area")

    # more info

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Text"
        verbose_name_plural = "More Text"
