from django import forms
from cars.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'O valor do veículo não pode ser inferior a R$ 20.000,00!')
        return value
    
    def clean_plate(self):
        plate = self.cleaned_data.get('plate')
        if len(plate) > 7:
            self.add_error('plate', 'A placa deve ter 7 caracteres!')
        return plate
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Não são aceitos veículos anteriores a 1975!')
        return factory_year