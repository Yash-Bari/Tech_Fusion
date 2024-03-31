from django import forms
from .models import Registration, Payment

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['event', 'full_name', 'email', 'whatsapp_number']
        widgets = {
            'event': forms.Select(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'whatsapp_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['transaction_id', 'screenshot']
        widgets = {
            'transaction_id': forms.TextInput(attrs={'class': 'form-control'}),
            'screenshot': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
