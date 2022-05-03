from django import forms


class TicketForm(forms.Form):
    title = forms.CharField(max_length=50, label='Título', widget=forms.TextInput(attrs={
        'placeholder': 'Título Mensaje',
        'class': 'form-control'
    }))

    text = forms.CharField(max_length=2000, label='Texto', widget=forms.Textarea(attrs={
        'placeholder': 'Ingrese el problema a resolver',
        'class': 'form-control',
    }))
