from django import forms

class TodoForm():
    text = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'A Django TODO List',
        }))
