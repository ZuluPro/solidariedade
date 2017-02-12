from django.conf.urls import url, patterns, include
from donation import views


urlpatterns = patterns(
    'donation.views',
    url(r'^$', views.DonationWizard.as_view(), name="donation"),
    url(r'^done/paypal$', views.PaypalDoneView.as_view(), name="donation-paypal-done"),
    url(r'^paypal/', include('paypal.standard.ipn.urls'))
)
