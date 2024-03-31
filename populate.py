# populate_events.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tech_fusion_2024.settings')
django.setup()

from event_registration.models import Event

events_data = [
    {"name": "Digital Poster competition", "entry_fee": 49, "is_team_event": False},
    {"name": "Handmade Poster competition", "entry_fee": 49, "is_team_event": False},
    {"name": "BGMI", "entry_fee": 200, "is_team_event": True},
    {"name": "Valorant", "entry_fee": 250, "is_team_event": True},
    {"name": "Treasure hunt", "entry_fee": 200, "is_team_event": True},
    {"name": "Project competition", "entry_fee": 150, "is_team_event": True},
    {"name": "Coding challenge", "entry_fee": 50, "is_team_event": False},
    {"name": "Tech quiz", "entry_fee": 100, "is_team_event": True},
    {"name": "Website design", "entry_fee": 59, "is_team_event": False},
]

for event_data in events_data:
    event = Event.objects.create(**event_data)
    print(f"Event '{event.name}' created.")
