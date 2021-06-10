from django.db import models

class Ss(models.Model):
    title = models.CharField(max_length=50, unique_for_date='published')
    published = models.DateTimeField()
    edited = models.DateTimeField()
    content = models.TextField(null = True, blank=True, verbose_name='Описание')

    class Kinds(models.TextChoices):
        BUY = 'b', 'Куплю'
        SELL = 's', 'Продам'
        EXCHANGE = 'с', 'Обменяю'
        RENT = 'r'
        __empty__ = 'Выберите тип публикуемого объявления'
    kind = models.CharField(max_length=1, choices = Kinds.choices, default=Kinds.SELL)

    class Meta:
        ordering = ['-published', 'title']
        unique_together = ('title', 'published')
        get_latest_by = ['edited’, ’published']