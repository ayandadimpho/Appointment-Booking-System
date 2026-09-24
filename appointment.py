def create_appointment(patient, provider, date, time):
    if not patient:
        raise ValueError("Patient name cannot be empty")

    if not provider:
        raise ValueError("Provider name cannot be empty")

    return {
        "patient": patient,
        "provider": provider,
        "date": date,
        "time": time
    }
