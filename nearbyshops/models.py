from django.contrib.gis.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    location = models.PointField()
    city = models.CharField(max_length=50)

'''
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Shops'

    def get_absolute_url(self):
        return reverse('shop-detail', args=[str(self.id)])

    def get_update_url(self):
        return reverse('shop-update', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('shop-delete', args=[str(self.id)
'''