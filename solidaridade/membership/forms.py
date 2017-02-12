from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django.utils.translation import ugettext_lazy as _
from membership import models

User = get_user_model()


class ContributionForm(forms.ModelForm):
    class Meta:
        model = models.Contribution
        exclude = ()


class MemberForm(forms.ModelForm):
    class Meta:
        model = models.Member
        exclude = ()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ()

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            msg = _("This email has already been registered")
            self.add_error('email', msg)
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username:
            username = (self.cleaned_data['first_name'][:2] + self.cleaned_data['last_name']).lower().replace(' ', '')[:30]
            if User.object.filter(username=username).exists():
                username = username[:29] + str(User.object.filter(username=username).count())
        return username


class BaseMemberPublicForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseMemberPublicForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            if 'class' not in self.fields[field_name].widget.attrs:
                self.fields[field_name].widget.attrs['class'] = 'form-control'
            else:
                self.fields[field_name].widget.attrs['class'] += 'form-control'
            self.fields[field_name].widget.attrs['placeholder'] = self.fields[field_name].help_text


class DonationTypeForm(forms.Form):
    donation_type = forms.CharField()


class CreateUserForm(BaseMemberPublicForm, UserForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'email',
        )


class SetPasswordForm(BaseMemberPublicForm):
    class Meta:
        model = get_user_model()
        fields = ('password',)
        widgets = {
            'password': forms.PasswordInput
        }

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.instance.set_password(password)
        if commit:
            self.instance.save()
        return self.instance


class MemberPublicStep2Form(BaseMemberPublicForm):
    class Meta:
        model = models.Member
        fields = (
            'country',
            'address',
            'postal_code',
            'city',
            'phone_number',
        )

    def __init__(self, *args, **kwargs):
        super(MemberPublicStep2Form, self).__init__(*args, **kwargs)


class DonationAmountForm(forms.Form):
    amount = forms.IntegerField()


class MembershipTitleForm(BaseMemberPublicForm):
    class Meta:
        model = models.Member
        fields = (
            'title',
        )


class ContributionPublicForm(forms.ModelForm):
    class Meta:
        model = models.Contribution
        fields = (
            'sum',
            'payment_method',
        )
