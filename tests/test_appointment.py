def test_create_appointment():
    from appointment import Apoointment

    appointment = Appointment(
        patient="Ayanda",
        provider="Dr Mtolo",
        date="2026-10-15",
        time="08:00"
    )

    assert appointment.patient == "Ayanda"
    assert appointment.provider == "Dr Mtolo"
    assert appointment.date == "2026-10-15"
    assert appointment.time == "08:00"