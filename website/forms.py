from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    tel = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        send_mail(
        'Contact from Website ' + self.cleaned_data['email'],
        'Name: ' + self.cleaned_data['name'] + "\n" +
        'Email: ' + self.cleaned_data['email'] + "\n" +
        'Tel: ' + self.cleaned_data['tel'] + "\n" +
        'Message: ' + self.cleaned_data['message'] + "\n",
        
        'info@ubihope.com',
        ['info@ubihope.com'],
        fail_silently=False,
        )   
        pass