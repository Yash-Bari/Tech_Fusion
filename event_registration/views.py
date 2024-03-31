from django.shortcuts import render, redirect
from .models import Event, Registration, Payment
from .forms import RegistrationForm, PaymentForm

def registration_view(request):
    events = Event.objects.all()  # Query all events from the database
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration = registration_form.save()
            return redirect('payment', registration_id=registration.pk)
    else:
        registration_form = RegistrationForm()
    return render(request, 'registration_form.html', {'registration_form': registration_form, 'events': events})

def payment_view(request, registration_id):
    registration = Registration.objects.get(pk=registration_id)
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST, request.FILES)
        if payment_form.is_valid():
            payment = payment_form.save(commit=False)
            payment.registration = registration
            payment.save()
            return redirect('success')
    else:
        payment_form = PaymentForm()
    return render(request, 'payment_form.html', {'payment_form': payment_form, 'registration_id': registration_id})

def success_view(request):
    return render(request, 'success_page.html')
