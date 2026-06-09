from django.shortcuts import render
from tracker.models import VehicleCount
from events.models import Event

def reports_dashboard(request):

    event = Event.objects.filter(
        active=True
    ).first()

    records = VehicleCount.objects.filter(
        event=event
    )

    total_bus = sum(
        x.count for x in records
        if x.vehicle_type == 'BUS'
    )

    total_coster = sum(
        x.count for x in records
        if x.vehicle_type == 'COSTER'
    )

    total_taxi = sum(
        x.count for x in records
        if x.vehicle_type == 'TAXI'
    )

    return render(
        request,
        'reports/report.html',
        {
            'event':event,
            'records':records,
            'total_bus':total_bus,
            'total_coster':total_coster,
            'total_taxi':total_taxi
        }
    )