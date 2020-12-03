from django import forms
from ..models import Unit


class AddRecipe(forms.Form):
    Name = forms.CharField(required=True, max_length=100,
                           widget=forms.TextInput(attrs={"placeholder": "Enter recipe name.."}))
    Ingredient = forms.CharField(required=True, max_length=64,
                                 widget=forms.TextInput(attrs={"placeholder": "Enter ingredient.."}))
    Quantity = forms.IntegerField()
    Unit = forms.ModelChoiceField(required=True,
                                  queryset=Unit.objects.all())
    CookingTime = forms.IntegerField(required=True, label="Cooking Time")
    Step = forms.IntegerField(required=True, label="Step Number")
    StepName = forms.CharField(required=True, max_length=100,
                               widget=forms.TextInput(attrs={"placeholder": "Enter step name.."}))
    Description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Enter procedure"}))

    def __init__(self, *args, **kwargs):
        super(AddRecipe, self).__init__(*args, **kwargs)
        self.fields['Name'].widget.attrs.update({'class': 'form-control'})
        self.fields['Ingredient'].widget.attrs.update({'class': 'form-control'})
        self.fields['Quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['Unit'].widget.attrs.update({'class': 'form-control'})
        self.fields['CookingTime'].widget.attrs.update({'class': 'form-control'})
        self.fields['Step'].widget.attrs.update({'class': 'form-control'})
        self.fields['StepName'].widget.attrs.update({'class': 'form-control'})
        self.fields['Description'].widget.attrs.update({'class': 'form-control'})

