from django import forms
from .models import Account, UserProfile

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Ingrese Password',
         'class' : 'form-control'
    }))
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirmar Password',
        'class' : 'form-control'
    }))
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
        
        
    def __init__(self, *arg, **kwargs):
        super(RegistrationForm, self).__init__(*arg, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Ingrese Nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Ingrese Apellidos'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Ingrese Teléfono'
        self.fields['email'].widget.attrs['placeholder'] = 'Ingrese Email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                "El password no coincide!"
            )
            
            
class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number')
        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            

class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages={'invalid' : ('Solo archivos Imagen')}, widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'profile_picture', 'vat', 'zip', 'bank', 'bank_account')
        
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'