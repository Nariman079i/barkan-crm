from django.db import models


class Customer(models.Model):
    surname = models.CharField("Фамилия", null=True, blank=True, max_length=255)
    name = models.CharField("Имя", null=True, blank=True, max_length=255)
    patronymic = models.CharField("Отчество", null=True, blank=True, max_length=255)

    tel = models.CharField("Номер телефона", null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        if not self.surname:
            return "Клиент"
        return f"{self.surname}"
    

class Service(models.Model):
    title = models.CharField("Наименование", null=True, blank=True,max_length=255)
    direct_description = models.CharField("Краткое описание", null=True, blank=True,max_length=255)
    description = models.TextField("Полное описание", null=True, blank=True,max_length=1000)
    price = models.IntegerField()

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        if not self.title:
            return "Услуга"
        return self.title
class Guide(models.Model):
    surname = models.CharField("Фамилия", null=True, blank=True, max_length=255)
    name = models.CharField("Имя", null=True, blank=True, max_length=255)
    patronymic = models.CharField("Отчество", null=True, blank=True, max_length=255)
    tel = models.CharField("Номер телефона", null=True, blank=True, max_length=255)
    salary = models.IntegerField("Зарплата", null=True, blank=True)

    class Meta:
        verbose_name = "Гид"
        verbose_name_plural = "Гиды"

    def __str__(self):
        if not self.name:
            return "Гид"
        return self.name
    

class History(models.Model):
    guide = models.ForeignKey(Guide,on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL,null=True)

    def __str__(self) -> str:
        if not self.guide:
            return "История "
        return self.guide
    
    