from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['nom', 'email', 'sujet', 'message']
        widgets = {
            'nom': forms.TextInput(attrs={
                'placeholder': 'Votre nom', 'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Votre adresse email', 'class': 'form-control'
            }),
            'sujet': forms.TextInput(attrs={
                'placeholder': 'Sujet de votre message', 'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Votre message', 'class': 'form-control', 'rows': 6
            }),
        }

    def clean_nom(self):
        nom = self.cleaned_data['nom'].strip()
        if len(nom) < 2:
            raise forms.ValidationError('Le nom doit contenir au moins 2 caractères.')
        return nom

    def clean_message(self):
        message = self.cleaned_data['message'].strip()
        if len(message) < 10:
            raise forms.ValidationError('Votre message doit contenir au moins 10 caractères.')
        return message
