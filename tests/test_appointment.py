from appointment import create_appointment
from tests import appointment

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
