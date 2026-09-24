from datetime import datetime

def create_appointment(patient, provider, date, time):
    if not patient:
        raise ValueError("Patient name cannot be empty")

    if not provider:
        raise ValueError("Provider name cannot be empty")

    if not date:
        raise ValueError("Appointment date cannot be empty")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Appointment date must use YYYY-MM-DD format")

    if not time:
        raise ValueError("Appointment time cannot be empty")

    return {
        "patient": patient,
        "provider": provider,
        "date": date,
        "time": time
    }
