from django import forms
from .models import Customer
from .models import Property

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone','maxPrice','minPrice',)


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('customer', 'prop_number', 'type', 'address', 'city', 'state', 'zipcode', 'squarefeet', 'price','image','bed','bath', 'build', 'purpose', 'status',)