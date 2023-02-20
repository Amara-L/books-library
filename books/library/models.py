from django.db import models


# Класс, описывающий модели сущностей БД
#   Country - сущность "Страна"
#       id : идентификатор, тип - int, автоинкремент, не может быть пустым
#       name : наименование страны, тип - строка, ограничение - 240 символов, не может быть пустым,
#           может содержать только уникальные значения
#   Author - сущность "Автор книги"
#       id : идентификатор, тип - int, автоинкремент, не может быть пустым
#       name : ФИО или псевдоним, тип - строка, ограничение - 240 символов, не может быть пустым
#       country : страна, тип - внешний ключ к сущности "Страна", не может быть пустым
#       dob : дата рождения, тип - дата, не может быть пустым
#   Publishing - сущность "Издательство"
#       id : идентификатор, тип - int, автоинкремент, не может быть пустым
#       name : наименование издательства, тип - строка, ограничение - 240 символов, не может быть пустым
#       country : страна, тип - внешний ключ к сущности "Страна", не может быть пустым
#   Book - сущность "Книга"
#       id : идентификатор, тип - int, автоинкремент, не может быть пустым
#       name : наименование книги, тип - строка, ограничение - 240 символов, не может быть пустым
#       description : описание книги, тип - строка, ограничение - 500 символов, не может быть пустым
#       instanceCount : количество изднанных экземпляров книги, тип - int
#       dateIssue : дата издания книги, тип - дата, не может быть пустым
#       author : автор книги, тип - внешний ключ к сущности "Автор книги", не может быть пустым
#       publishing : издательство, тип - внешний ключ к сущности "Издательство", не может быть пустым
#       instanceCount : количество страниц книги, тип - int


class Country(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=240, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class Author(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=240, blank=False, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=False, null=False)
    dob = models.DateField(blank=False)

    def __str__(self):
        return self.name


class Publishing(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=240, blank=False, null=False)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT, blank=False, null=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=240, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    instanceCount = models.IntegerField()
    dateIssue = models.DateField(blank=False)
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    publishing = models.ForeignKey(Publishing, on_delete=models.RESTRICT)
    pages = models.IntegerField()

    def __str__(self):
        return self.name


