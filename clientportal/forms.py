from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50, label='Nombre', widget=forms.TextInput(attrs={
        'placeholder' : 'Ingrese su nombre',
         'class' : 'form-control'
    }))
    
    last_name = forms.CharField(max_length = 50, label='Apellido', widget=forms.TextInput(attrs={
        'placeholder' : 'Ingrese su nombre',
         'class' : 'form-control'
    }))
    
    phone = forms.CharField(max_length = 50, label='Teléfono', widget=forms.TextInput(attrs={
        'placeholder' : 'Ingrese su Teléfono',
         'class' : 'form-control'
    }))
    
    email_address = forms.CharField(max_length = 50, label='Email', widget=forms.EmailInput(attrs={
        'placeholder' : 'Ingrese su Correo',
         'class' : 'form-control'
    }))
    
    message = forms.CharField(max_length = 2000, label='Mensaje', widget=forms.Textarea(attrs={
        'placeholder' : 'Ingrese su mensaje',
         'class' : 'form-control',
    }))