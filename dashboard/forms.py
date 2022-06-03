from django import forms


class DashboardForm(forms.Form):
    text = forms.CharField(max_length=200, label="Enter Your Search :")
