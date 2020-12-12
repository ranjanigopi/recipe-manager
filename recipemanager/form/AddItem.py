from django import forms

from ..models import Unit


class AddItem(forms.Form):
    Name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={"placeholder": "Enter ingredient name.."}))
    Quantity = forms.IntegerField(required=True,
                                  widget=forms.NumberInput(attrs={"placeholder": "Enter quantity..", "min_value": "0"}))
    Unit = forms.ModelChoiceField(required=True,
                                  queryset=Unit.objects.all())


