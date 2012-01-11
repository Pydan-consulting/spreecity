from django.contrib.auth.models import User

from django import forms

class MemberForm(forms.Form):
    first_name          = forms.CharField()
    last_name           = forms.CharField()
    country             = forms.ChoiceField(choices = [('SINGAPORE','Singapore'),('SINGAPORE','Singapore')])
    city                = forms.ChoiceField(choices = [('SINGAPORE','Singapore'),('SINGAPORE','Singapore')])
    email               = forms.EmailField()
    password            = forms.CharField( widget=forms.PasswordInput)
    confirm_password    = forms.CharField( widget=forms.PasswordInput)
    date                = forms.ChoiceField(choices = [('1','1'),('2','2')])
    month               = forms.ChoiceField(choices = [('1','JAN'),('2','FEB')])
    year                = forms.ChoiceField(choices = [('1980','1980'),('1981','1981'),('1982','1982')])
    

    def clean_email(self):
        email = self.cleaned_data['email']
        user_check = User.objects.filter(email = email)
        if len(user_check) > 0:
            raise forms.ValidationError("Email already available in the system")
        return email
    
class PartnerForm(forms.Form):
    company_name            = forms.CharField()
    company_country         = forms.ChoiceField(choices = [('SINGAPORE','Singapore'),('SINGAPORE','Singapore')])
    business_name           = forms.CharField()
    business_type           = forms.ChoiceField(choices = [('FASHION','FASHION'),('IT','IT')])
    business_description    = forms.CharField(widget=forms.Textarea)
    mailling_address        = forms.CharField(widget=forms.Textarea)
    zipcode                 = forms.CharField()
    country                 = forms.ChoiceField(choices = [('SINGAPORE','Singapore'),('SINGAPORE','Singapore')])
    state                   = forms.CharField()
    city                    = forms.CharField()
    #email                   = forms.EmailField()
    #password                = forms.CharField( widget=forms.PasswordInput)
    #confirm_password        = forms.CharField( widget=forms.PasswordInput)
    #update                  = forms.BooleanField(label = 'I would like to receive updates from SpreeCity', initial = True)
    
    def clean_email(self):
        email = self.cleaned_data['email']
        user_check = User.objects.filter(email = email)
        if len(user_check) > 0:
            raise forms.ValidationError("Email already available in the system")
        return email