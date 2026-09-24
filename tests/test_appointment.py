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