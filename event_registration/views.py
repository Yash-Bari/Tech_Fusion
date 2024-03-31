from django.shortcuts import render, redirect
from .models import Event, Registration, Payment
from .forms import RegistrationForm, PaymentForm

def registration_view(request):
    events = Event.objects.all()  # Query all events from the database
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            event_id = request.POST.get('event')  # Get the selected event ID from the form data
            event = Event.objects.get(pk=event_id)  # Get the event object
            full_name = registration_form.cleaned_data['full_name']
            email = registration_form.cleaned_data['email']
            whatsapp_number = registration_form.cleaned_data['whatsapp_number']
            # Check if it's a team event
            if event.is_team_event:
                team_members = []
                for i in range(1, 6):  # Assuming maximum of 5 team members
                    team_member_name = request.POST.get(f'team_member_{i}')
                    if team_member_name:
                        team_members.append(team_member_name)
                registration = Registration.objects.create(event=event, full_name=full_name, email=email, whatsapp_number=whatsapp_number, team_members=team_members)
            else:
                registration = Registration.objects.create(event=event, full_name=full_name, email=email, whatsapp_number=whatsapp_number)
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
