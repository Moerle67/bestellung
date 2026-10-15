from django.db import models
from django.urls import reverse

# Create your models here.

class Menuart(models.Model):
    name = models.CharField("Menü Art:", max_length=50)
    short = models.CharField("Kürzel", max_length=10)
    description = models.TextField("Beschreibung", blank=True, null=True)

    class Meta:
        verbose_name = "Menuart"
        verbose_name_plural = "Menuarten"

    def __str__(self):
        return self.short

    def get_absolute_url(self):
        return reverse("Menuart_detail", kwargs={"pk": self.pk})

class Menue(models.Model):
    date = models.DateField("Datum ", auto_now=False, auto_now_add=False)
    art = models.ForeignKey(Menuart, verbose_name="Menueart", on_delete=models.CASCADE)
    description = models.TextField("Beschreibung")

    class Meta:
        verbose_name = "Menü"
        verbose_name_plural = "Menüs"

    
    def __str__(self):
        return f"{self.date}/{self.art.short}"

    def get_absolute_url(self):
        return reverse("Menue_detail", kwargs={"pk": self.pk})

class Team(models.Model):
    name = models.CharField("Name", max_length=50)
    description = models.TextField("Beschreibung", blank=True, null=True)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Team_detail", kwargs={"pk": self.pk})
    
class Order(models.Model):
    team = models.ForeignKey(Team, verbose_name="Gruppe", on_delete=models.CASCADE)
    menu = models.ForeignKey(Menue, verbose_name="Menü", on_delete=models.CASCADE)
    anzahl = models.IntegerField("Anzahl")
    date_order = models.DateField("Zeitpunkt der Bestellung", auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "Bestellung"
        verbose_name_plural = "Bestellung"
        ordering = ['-date_order', 'menue']

    def __str__(self):
        return f"{self.menu}/{self.team} - {self.anzahl}"

    def get_absolute_url(self):
        return reverse("Order_detail", kwargs={"pk": self.pk})
