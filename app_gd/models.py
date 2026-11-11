from django.db import models

# CREATE TABLE fruit
# (
# 	id uuid default gen_random_uuid (),
# 	title text,
# 	weight real default 0.0,
# 	price integer default 0,
# 	primary key (id)
# );

# INSERT INTO fruit (title, weight, price) VALUES
# 	('Яблоки', 1.0, 35),
# 	('Груши', 1.0, 32),
# 	('Абрикосы', 1.0, 45),
# 	('Апельсины', 1.0, 39);

# Create your models here.

class Fruit(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.TextField(verbose_name="Название")
    weight = models.FloatField(verbose_name="Вес")
    price = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return self.title


