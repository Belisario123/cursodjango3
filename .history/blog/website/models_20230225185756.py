from django.db import models

class YearInSchool(models.TextChoices):
    FRESHMAN = 'FR', _('Freshman')
    SOPHOMORE = 'SO', _('Sophomore')
    FRESHMAN = 'FR', _('Freshman')
    FRESHMAN = 'FR', _('Freshman')
    FRESHMAN = 'FR', _('Freshman')


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    
    def full_name(self):
        return self.title + self.sub_title
    
    full_name.admin_order_field = 'title'


