from django import forms


class AddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=10)
