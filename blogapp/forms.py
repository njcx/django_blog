from django import forms



class ContactForm(forms.Form):
    user_name = forms.CharField(max_length=20)
    qq = forms.IntegerField(required=False)
    wechat = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(required=False)
    content = forms.CharField(max_length=2000)
    phone = forms.IntegerField(required=False)