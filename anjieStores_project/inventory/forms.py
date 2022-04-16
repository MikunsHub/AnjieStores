from django import forms
from .models import ItemCount

class ItemForm(forms.Form):
    productqty = forms.CharField(max_length=30)
    
    

    def clean(self):
        cleaned_data = super(ItemForm, self).clean()
        productqty = cleaned_data.get('productqty')
        if not productqty :
            raise forms.ValidationError('You have to write something!')

