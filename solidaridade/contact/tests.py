from django.test import TestCase
from django.core import mail
from .forms import ContactForm


class ContactFormTest(TestCase):
    def test_send_mail(self):
        data = {
            'name': "Foo",
            'email': "foo@bar.com",
            'message': "It is a dummy message, really dummy!"
        }
        form = ContactForm(data)
        form.is_valid()
        form.send_mail()
        self.assertEqual(len(mail.outbox), 1)
