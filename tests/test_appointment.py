import pytest

from appointment import create_appointment

def test_create_appointment():
    appointment = create_appointment(
        patient="Ayanda",
        provider="Dr Mtolo",
        date="2026-10-15",
        time="08:00"
    )

    assert appointment["patient"] == "Ayanda"
    assert appointment["provider"] == "Dr Mtolo"
    assert appointment["date"] == "2026-10-15"
    assert appointment["time"] == "08:00"

def test_appointment_rejects_empty_patient_name():
    try:
        create_appointment(
            "",
            "Dr Mtolo",
            "2026-10-15",
            "08:00"
        )
        assert False
    except ValueError:
        assert True


def test_appointment_rejects_empty_provider_name():
    try:
        create_appointment(
            "Ayanda",
            "",
            "2026-10-01",
            "10:00"
        )
        assert False
    except ValueError:
        assert True


def test_create_appointment():
    appointment = create_appointment(
        patient="Ayanda",
        provider="Dr Mtolo",
        date="2026-10-15",
        time="08:00"
    )

    assert appointment["patient"] == "Ayanda"
    assert appointment["provider"] == "Dr Mtolo"
    assert appointment["date"] == "2026-10-15"
    assert appointment["time"] == "08:00"

def test_appointment_rejects_empty_patient_name():
    try:
        create_appointment(
            "",
            "Dr Mtolo",
            "2026-10-15",
            "08:00"
        )
        assert False
    except ValueError:
        assert True


def test_appointment_rejects_empty_provider_name():
    try:
        create_appointment(
            "Ayanda",
            "",
            "2026-10-01",
            "10:00"
        )
        assert False
    except ValueError:
        assert True


def test_create_appointment():
    appointment = create_appointment(
        patient="Ayanda",
        provider="Dr Mtolo",
        date="2026-10-15",
        time="08:00"
    )

    assert appointment["patient"] == "Ayanda"
    assert appointment["provider"] == "Dr Mtolo"
    assert appointment["date"] == "2026-10-15"
    assert appointment["time"] == "08:00"

def test_appointment_rejects_empty_patient_name():
    try:
        create_appointment(
            "",
            "Dr Mtolo",
            "2026-10-15",
            "08:00"
        )
        assert False
    except ValueError:
        assert True


def test_appointment_rejects_empty_provider_name():
    try:
        create_appointment(
            "Ayanda",
            "",
            "2026-10-01",
            "10:00"
        )
        assert False
    except ValueError:
        assert True

def test_appointment_rejects_empty_date():
    with pytest.raises(ValueError):
        create_appointment(
            "Ayanda",
            "Dr Mtolo",
            "",
            "08:00"
        )


def test_appointment_rejects_empty_time():
    with pytest.raises(ValueError):
        create_appointment(
            "Ayanda",
            "Dr Mtolo",
            "2026-10-15",
            ""
        )

def test_appointment_rejects_invalid_date_format():
    with pytest.raises(ValueError):
        create_appointment(
            "Ayanda",
            "Dr Mtolo",
            "15-10-2026",
            "08:00"
        )

def test_appointment_rejects_invalid_time_format():
    with pytest.raises(ValueError):
        create_appointment(
            "Ayanda",
            "Dr Mtolo",
            "2026-10-15",
            "8:00 AM"
        )
