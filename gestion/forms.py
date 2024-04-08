from django import forms

class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=150),
    description = forms.Textarea(),
    price = forms.DecimalField(decimal_places=2, max_digits=5)
