from django import forms


class ViewForm(forms.Form):
    Student_ID = forms.CharField(max_length=200)
    Notifications = forms.CharField(widget=forms.Textarea, required=True)
