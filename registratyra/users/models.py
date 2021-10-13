from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=30)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30)
    second_name = models.CharField(verbose_name='Отчество', max_length=30)
    ROLES = (
        ('PATIENT', 'Пациент'),
        ('DOCTOR', 'Врач'))
    role = models.CharField(verbose_name='Роль', choices=ROLES, default='PATIENT', max_length=100)
    is_superuser = models.BooleanField(verbose_name='Администратор', default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.second_name}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Patient(models.Model):
    user = models.ForeignKey('User', verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'


class Speciality(models.Model):
    name = models.CharField(verbose_name='Название врачебной специализации', max_length=255)

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.ForeignKey('User', verbose_name='Пользователь', on_delete=models.CASCADE)
    speciality = models.ForeignKey('Speciality', verbose_name='Специализация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.speciality.__str__().lower()}, {self.user}'

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
