from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    pages = models.IntegerField()
    pics = models.IntegerField()
    cost = models.IntegerField()

    def __str__(self):
        return self.name
    #    return self.name + ' автор: ' + str(self.author) + ' курс: ' + str(self.course)


class Library(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    #def __str__(self):
     #   return 'комната на этаже №' + str(self.floor) + ' с вместимостью ' + str(self.capacity)


class BookInLib(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    bookname = book.name
    lib = models.ForeignKey(Library, on_delete=models.CASCADE)
    copies = models.IntegerField(default=0)
    students = models.IntegerField(default=0)
    departments = models.CharField(max_length=100, default='None')
    def __str__(self):
        return str(self.book) + ' в библиотеке ' + str(self.lib)
