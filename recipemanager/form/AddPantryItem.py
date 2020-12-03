from django import forms

from ..models import Unit

# Add ingredients to make recipe


class AddPantryItem(forms.Form):
    Name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={"placeholder": "Enter ingredient name.."}))
    Quantity = forms.IntegerField(required=True,
                                  widget=forms.NumberInput(attrs={"placeholder": "Enter quantity..", "min_value": "0"}))
    Unit = forms.ModelChoiceField(required=True,
                                  queryset=Unit.objects.all())

    def __init__(self, *args, **kwargs):
        super(AddPantryItem, self).__init__(*args, **kwargs)
        self.fields['Name'].widget.attrs.update({'class': 'form-control'})
        self.fields['Quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['Unit'].widget.attrs.update({'class': 'form-control'})


