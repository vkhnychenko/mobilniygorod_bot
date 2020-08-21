from django.db import models


class ManualCategory(models.Model):
    name = models.CharField('Название мануала', max_length=150)
    is_active = models.BooleanField('Показ мануала', default=True)


class ManualItem(models.Model):
    description = models.TextField('Описание')
    image = models.ImageField('Картинка', upload_to='manuals/')
    #related name позволяет обратиться из связующей таблицы
    category = models.ForeignKey(ManualCategory, verbose_name='Мануал', on_delete=models.CASCADE, null=True, related_name='items')
