from sqlalchemy.orm import Session

from models.appointment import Appointment


def create_appointment(
    db: Session,
    appointment: Appointment,
):
    

    db.add(appointment)

    db.commit()

    db.refresh(appointment)

    return appointment


def get_all_appointments(
    db: Session,
):

    return (

        db.query(Appointment)

        .filter(
            Appointment.is_active == True
        )

        .all()

    )


def get_appointment_by_id(
    db: Session,
    appointment_id: int,
):

    return (

        db.query(Appointment)

        .filter(
            Appointment.id == appointment_id
        )

        .first()

    )


def get_appointment_count(
    db: Session,
):

    return (

        db.query(Appointment)

        .count()

    )
def get_doctor_appointment(
    db: Session,
    doctor_id: int,
    appointment_datetime,
):

    return (

        db.query(Appointment)

        .filter(
            Appointment.doctor_id == doctor_id,
            Appointment.appointment_datetime == appointment_datetime,
            Appointment.is_active == True,
        )

        .first()

    )

def update_appointment(
    db: Session,
    appointment: Appointment,
):

    db.commit()

    db.refresh(appointment)

    return appointment


def delete_appointment(
    db: Session,
    appointment: Appointment,
):

    appointment.is_active = False

    db.commit()

    db.refresh(appointment)

    return appointment