from datetime import timedelta
from urlparse import urljoin

from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.core.urlresolvers import reverse
from django.contrib.auth import forms as auth_forms
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.contrib.auth import get_user_model

from formtools.wizard.views import SessionWizardView
from paypal.standard.forms import PayPalPaymentsForm

from membership import forms

User = get_user_model()
BASE_URL = 'http://solidariedade-france-portugal.org/'


def show_paypal(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('donation') or {}
    return cleaned_data.get('payment_method') == 'paypal'


def show_amount(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('base') or {}
    return cleaned_data.get('donation_type') == 'donation'


def show_title(wizard):
    return not show_amount(wizard)


TEMPLATES = {"base": "donation.html",
             "paypal": "donation_paypal.html"}


class DonationWizard(SessionWizardView):
    form_list = [
        ('base', forms.DonationTypeForm),
        ('user_create', forms.CreateUserForm),
        ('user_create_password', forms.SetPasswordForm),
        ('address', forms.MemberPublicStep2Form),

        ('donation', forms.ContributionPublicForm),
        ('membership', forms.MembershipTitleForm),

        ('paypal', PayPalPaymentsForm)
    ]
    condition_dict = {
        'amount': show_amount,
        'membership': show_title,
        'paypal': show_paypal,
    }

    def get_template_names(self):
        if self.steps.current in TEMPLATES:
            return [TEMPLATES[self.steps.current]]
        return 'donation_form.html'

    def get_context_data(self, form, **kwargs):
        context = super(DonationWizard, self).get_context_data(form=form, **kwargs)
        if self.steps.current == 'paypal':
            amount = str(self.get_cleaned_data_for_step('donation')['sum'])
            item_name = self.get_cleaned_data_for_step('base')['donation_type']
            user_data = self.get_cleaned_data_for_step('user_create')
            address_data = self.get_cleaned_data_for_step('address')
            invoice = ''
            paypal_dict = {
                "business": "receiver_email@example.com",
                "amount": amount,
                "item_name": item_name,
                "invoice": invoice,
                "currency_code": 'EUR',
                "notify_url": urljoin(BASE_URL, reverse('paypal-ipn')),
                "return_url": 'http://solidariedade-france-portugal.org:8080/donation/done/paypal', # urljoin(BASE_URL, reverse('donation-paypal-done')),
                "cancel_return": self.request.get_raw_uri(),
                "no_shipping": 1,

                "email": user_data['email'],
                "first_name": user_data['first_name'],
                "last_name": user_data['last_name'],
                "country": address_data['country'],
                "city": address_data['city'],
                "address1": address_data['address'],
                "zip": address_data['postal_code'],
            }
            form = PayPalPaymentsForm(initial=paypal_dict)
            context['form'] = context['wizard']['form'] = form
        return context

    def done(self, form_list, **kwargs):
        # Create user
        user_data = {}
        user_data.update(self.get_cleaned_data_for_step('user_create'))
        user_data.update(self.get_cleaned_data_for_step('user_create_password'))
        user_data['date_joined'] = now()
        user_form = forms.UserForm(data=user_data)
        user_form.is_valid()
        user = user_form.save()
        user.set_password(user_data['password'])
        # Create member
        member_data = {}
        member_data.update(self.get_cleaned_data_for_step('address'))
        if show_amount(self):
            member_data.update({
                'user': user.id,
                'title': 1,
                'subscription_date': now(),
            })
        member_form = forms.MemberForm(member_data)
        member_form.is_valid()
        member = member_form.save()
        # Create contribution
        contrib_data = {
            'member': member.id,
            'due_date': now() + timedelta(days=31),
        }
        if show_amount(self):
            contrib_data.update(self.get_cleaned_data_for_step('donation'))
        else:
            contrib_data['sum'] = member.title.entry_fees
        contribution_form = forms.ContributionForm(contrib_data)
        contribution_form.is_valid()
        contribution = contribution_form.save()

        template_name = 'donation/%s_done.html' % contrib_data['payment_method']
        return render(self.request, template_name, {
            'member': member,
            'contribution': contribution,
        })


class PaypalDoneView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(PaypalDoneView, self).dispatch(*args, **kwargs)

    def post(self, request):
        import ipdb; ipdb.set_trace()
