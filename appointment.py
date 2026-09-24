from datetime import datetime


def create_appointment(patient, provider, date, time):
    if not patient:
        raise ValueError("Patient name cannot be empty")

    if not provider:
        raise ValueError("Provider name cannot be empty")

    if not date:
        raise ValueError("Appointment date cannot be empty")

    try:
        appointment_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Appointment date must use YYYY-MM-DD format")

    if appointment_date < datetime.today().date():
        raise ValueError("Appointment date cannot be in the past")

    if not time:
        raise ValueError("Appointment time cannot be empty")

    try:
        datetime.strptime(time, "%H:%M")
    except ValueError:
        raise ValueError("Appointment time must use HH:MM format")

    return {
        "patient": patient,
        "provider": provider,
        "date": date,
        "time": time
    }


def book_appointment(appointments, new_appointment):
    for existing_appointment in appointments:
        if (
            existing_appointment["provider"] == new_appointment["provider"]
            and existing_appointment["date"] == new_appointment["date"]
            and existing_appointment["time"] == new_appointment["time"]
        ):
            raise ValueError("Appointment slot is already booked")

    new_appointment["status"] = "booked"
    appointments.append(new_appointment)
    return new_appointment


def cancel_appointment(appointments, patient, provider, date, time):
    for existing_appointment in appointments:
        if (
            existing_appointment["patient"] == patient
            and existing_appointment["provider"] == provider
            and existing_appointment["date"] == date
            and existing_appointment["time"] == time
        ):
            existing_appointment["status"] = "cancelled"
            return existing_appointment

    raise ValueError("Appointment not found")


def is_provider_available(appointments, provider, date, time):
    for existing_appointment in appointments:
        if (
            existing_appointment["provider"] == provider
            and existing_appointment["date"] == date
            and existing_appointment["time"] == time
            and existing_appointment["status"] == "booked"
        ):
            return False

    return True