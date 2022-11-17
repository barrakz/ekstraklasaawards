from django.db import models


# kategorie nagród z opisem
class Category(models.Model):
    name = models.CharField(max_length=50)
    category_description = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Nomination(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.category}'
