from django import forms


class MessageForm(forms.Form):
    identity = forms.CharField()
    text = forms.CharField(label="Message", widget=forms.Textarea)
