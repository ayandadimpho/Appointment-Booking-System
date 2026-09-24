import pytest
import appointment


def test_create_appointment():
    new_appointment = appointment.create_appointment(
        patient="Ayanda",
        provider="Dr Mtolo",
        date="2026-10-15",
        time="08:00"
    )

    assert new_appointment["patient"] == "Ayanda"
    assert new_appointment["provider"] == "Dr Mtolo"
    assert new_appointment["date"] == "2026-10-15"
    assert new_appointment["time"] == "08:00"


def test_appointment_rejects_empty_patient_name():
    with pytest.raises(ValueError):
        appointment.create_appointment(
            "",
            "Dr Mtolo",
            "2026-10-15",
            "08:00"
        )


def test_appointment_rejects_empty_provider_name():
    with pytest.raises(ValueError):
        appointment.create_appointment(
            "Ayanda",
            "",
            "2026-10-01",
            "10:00"
        )


def test_appointment_rejects_empty_date():
    with pytest.raises(ValueError):
        appointment.create_appointment(
            "Ayanda",
            "Dr Mtolo",
            "",
            "08:00"
        )


def test_appointment_rejects_empty_time():
    with pytest.raises(ValueError):
        appointment.create_appointment(
            "Ayanda",
            "Dr Mtolo",
            "2026-10-15",
            ""
        )


def test_appointment_rejects_invalid_date_format():
    with pytest.raises(ValueError):
        appointment.create_appointment(
            "Ayanda",
            "Dr Mtolo",
            "15-10-2026",
            "08:00"
        )


def test_appointment_rejects_invalid_time_format():
    with pytest.raises(ValueError):
        appointment.create_appointment(
            "Ayanda",
            "Dr Mtolo",
            "2026-10-15",
            "8:00 AM"
        )


def test_appointment_rejects_past_date():
    with pytest.raises(ValueError):
        appointment.create_appointment(
            "Ayanda",
            "Dr Mtolo",
            "2020-01-01",
            "08:00"
        )


def test_book_appointment():
    appointments = []

    new_appointment = appointment.create_appointment(
        "Ayanda",
        "Dr Mtolo",
        "2026-10-15",
        "08:00"
    )

    booked = appointment.book_appointment(
        appointments,
        new_appointment
    )

    assert booked == new_appointment
    assert new_appointment in appointments


def test_cannot_book_same_provider_at_same_time():
    appointments = []

    first_appointment = appointment.create_appointment(
        "Ayanda",
        "Dr Mtolo",
        "2026-10-15",
        "08:00"
    )

    second_appointment = appointment.create_appointment(
        "Thabo",
        "Dr Mtolo",
        "2026-10-15",
        "08:00"
    )

    appointment.book_appointment(appointments, first_appointment)

    with pytest.raises(ValueError):
        appointment.book_appointment(appointments, second_appointment)

def test_cancel_appointment():
    appointments = []

    new_appointment = appointment.create_appointment(
        "Ayanda",
        "Dr Mtolo",
        "2026-10-15",
        "08:00"
    )

    appointment.book_appointment(appointments, new_appointment)

    cancelled = appointment.cancel_appointment(
        appointments,
        "Ayanda",
        "Dr Mtolo",
        "2026-10-15",
        "08:00"
    )

    assert cancelled["status"] == "cancelled"


def test_cannot_cancel_nonexistent_appointment():
    appointments = []

    with pytest.raises(ValueError):
        appointment.cancel_appointment(
            appointments,
            "Ayanda",
            "Dr Mtolo",
            "2026-10-15",
            "08:00"
        )

def test_booked_appointment_has_booked_status():
    appointments = []

    new_appointment = appointment.create_appointment(
        "Ayanda",
        "Dr Mtolo",
        "2026-10-15",
        "08:00"
    )

    booked = appointment.book_appointment(
        appointments,
        new_appointment
    )

    assert booked["status"] == "booked"


def test_provider_is_available_when_slot_is_not_booked():
    appointments = []

    available = appointment.is_provider_available(
        appointments,
        "Dr Mtolo",
        "2026-10-15",
        "08:00"
    )

    assert available is True

def test_provider_is_not_available_when_slot_is_booked():
    appointments = []

    new_appointment = appointment.create_appointment(
        "Ayanda",
        "Dr Mtolo",
        "2026-10-15",
        "08:00"
    )

    appointment.book_appointment(appointments, new_appointment)

    available = appointment.is_provider_available(
        appointments,
        "Dr Mtolo",
        "2026-10-15",
        "08:00"
    )

    assert available is False

def test_provider_is_available_after_appointment_is_cancelled():
    appointments = []

    new_appointment = appointment.create_appointment(
        "Ayanda",
        "Dr Mtolo",
        "2026-10-15",
        "08:00"
    )

    appointment.book_appointment(appointments, new_appointment)

    appointment.cancel_appointment(
        appointments,
        "Ayanda",
        "Dr Mtolo",
        "2026-10-15",
        "08:00"
    )

    available = appointment.is_provider_available(
        appointments,
        "Dr Mtolo",
        "2026-10-15",
        "08:00"
    )

    assert available is True

def test_appointment_accepts_today_date():
    from datetime import datetime

    today = datetime.today().strftime("%Y-%m-%d")

    new_appointment = appointment.create_appointment(
        "Ayanda",
        "Dr Mtolo",
        today,
        "08:00"
    )

    assert new_appointment["date"] == today

def test_appointment_accepts_midnight_time():
    new_appointment = appointment.create_appointment(
        "Ayanda",
        "Dr Mtolo",
        "2026-10-15",
        "00:00"
    )

    assert new_appointment["time"] == "00:00"

def test_appointment_accepts_end_of_day_time():
    new_appointment = appointment.create_appointment(
        "Ayanda",
        "Dr Mtolo",
        "2026-10-15",
        "23:59"
    )

    assert new_appointment["time"] == "23:59"

def test_appointment_rejects_impossible_calendar_date():
    with pytest.raises(ValueError):
        appointment.create_appointment(
            "Ayanda",
            "Dr Mtolo",
            "2026-02-30",
            "08:00"
        )

def test_appointment_rejects_invalid_hour():
    with pytest.raises(ValueError):
        appointment.create_appointment(
            "Ayanda",
            "Dr Mtolo",
            "2026-10-15",
            "24:00"
        )

def test_appointment_rejects_invalid_minute():
    with pytest.raises(ValueError):
        appointment.create_appointment(
            "Ayanda",
            "Dr Mtolo",
            "2026-10-15",
            "08:60"
        )

def test_complete_appointment_workflow():
    appointments = []

    new_appointment = appointment.create_appointment(
        "Ayanda",
        "Dr Mtolo",
        "2026-10-15",
        "08:00"
    )

    appointment.book_appointment(
        appointments,
        new_appointment
    )

    assert appointment.is_provider_available(
        appointments,
        "Dr Mtolo",
        "2026-10-15",
        "08:00"
    ) is False

    appointment.cancel_appointment(
        appointments,
        "Ayanda",
        "Dr Mtolo",
        "2026-10-15",
        "08:00"
    )

    assert appointment.is_provider_available(
        appointments,
        "Dr Mtolo",
        "2026-10-15",
        "08:00"
    ) is True