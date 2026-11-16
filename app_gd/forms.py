from .models import Fruit
from django.forms import *

class FruitForm(ModelForm):
    # title = TextInput(attrs={'class': 'fruit_class'})
    # weight = NumberInput()
    # price = NumberInput()

    def is_valid(self):
        valid = super().is_valid()
        return valid

    class Meta:
        model = Fruit
        fields = ["title", "weight", "price"]
        widgets = {
            "title": TextInput(attrs={
                                    'class': 'fruit_form',
                                    'placeholder': 'Введите название'
                                    }),
            "weight": NumberInput(attrs={
                                    'class': 'fruit_form',
                                    'placeholder': 'Введите вес'
                                    }),
            "price": NumberInput(attrs={
                                    'class': 'fruit_form',
                                    'placeholder': 'Введите цену'
                                    })
        }


