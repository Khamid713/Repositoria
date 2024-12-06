from django.db import models

# Create your models here.
#Таблица категорий
class Category(models.Model):
    category_name = models.CharField(max_length=64)
    def __str__(self):
        return str(self.category_name)


#Таблица продуктов
class News(models.Model):
    news_name = models.CharField(max_length=256)
    news_des = models.TextField()
    news_photo = models.ImageField()
    news_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.news_name)


