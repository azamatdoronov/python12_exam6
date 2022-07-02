from django.db import models

# Create your models here.
STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Guest_book(models.Model):
    author = models.CharField(max_length=20, null=False, blank=False, default="Unknown", verbose_name="Имя автора")
    email = models.EmailField(max_length=20, null=False, blank=False, default="No Email", verbose_name="Эл. почта")
    note = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Запись")
    created_nt = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_nt = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0],
                              verbose_name="Статус")

    def __str__(self):
        return f"{self.id}. {self.status}: {self.author} {self.note} {self.email}"

    class Meta:
        db_table = "guestbook"
        verbose_name = "запись"
        verbose_name_plural = "Список записей"
