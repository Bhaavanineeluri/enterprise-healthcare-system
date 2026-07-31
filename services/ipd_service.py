from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.ipd import IPD
from models.user import User

from repositories.ipd_repository import (
    create_ipd,
    delete_ipd,
    get_all_ipd,
    get_ipd_by_bed,
    get_ipd_by_id,
    get_ipd_count,
    update_ipd,
)

from repositories.patient_repository import (
    get_patient_by_id,
)

from repositories.doctor_repository import (
    get_doctor_by_id,
)

from repositories.department_repository import (
    get_department_by_id,
)

from repositories.ward_repository import (
    get_ward_by_id,
)

from repositories.room_repository import (
    get_room_by_id,
)

from repositories.bed_repository import (
    get_bed_by_id,
    update_bed,
)

from schemas.ipd_schema import (
    IPDCreate,
    IPDUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_ipd_code(
    db: Session,
):

    count = get_ipd_count(db)

    return f"IPD{count + 1:06d}"


def create_ipd_service(
    db: Session,
    ipd: IPDCreate,
    current_user: User,
):

    patient = get_patient_by_id(
        db,
        ipd.patient_id,
    )

    if patient is None:

        not_found(
            "Patient not found."
        )

    doctor = get_doctor_by_id(
        db,
        ipd.doctor_id,
    )

    if doctor is None:

        not_found(
            "Doctor not found."
        )

    department = get_department_by_id(
        db,
        ipd.department_id,
    )

    if department is None:

        not_found(
            "Department not found."
        )

    ward = get_ward_by_id(
        db,
        ipd.ward_id,
    )

    if ward is None:

        not_found(
            "Ward not found."
        )

    room = get_room_by_id(
        db,
        ipd.room_id,
    )

    if room is None:

        not_found(
            "Room not found."
        )

    bed = get_bed_by_id(
        db,
        ipd.bed_id,
    )

    if bed is None:

        not_found(
            "Bed not found."
        )

    existing = get_ipd_by_bed(
        db,
        ipd.bed_id,
    )

    if existing:

        bad_request(
            "Bed is already occupied."
        )

    new_ipd = IPD(

        ipd_code=generate_ipd_code(db),

        patient_id=ipd.patient_id,

        doctor_id=ipd.doctor_id,

        department_id=ipd.department_id,

        ward_id=ipd.ward_id,

        room_id=ipd.room_id,

        bed_id=ipd.bed_id,

        admission_date=ipd.admission_date,

        expected_discharge_date=ipd.expected_discharge_date,

        admission_reason=ipd.admission_reason,

        remarks=ipd.remarks,

        status="ADMITTED",
    )

    ipd_data = create_ipd(
        db,
        new_ipd,
    )

    bed.status = "OCCUPIED"

    update_bed(
        db,
        bed,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="IPD",
        action="CREATE",
    )

    return ipd_data


def get_all_ipd_service(
    db: Session,
    current_user: User,
):

    return get_all_ipd(db)


def get_ipd_service(
    db: Session,
    ipd_id: int,
    current_user: User,
):

    ipd = get_ipd_by_id(
        db,
        ipd_id,
    )

    if ipd is None:

        not_found(
            "IPD record not found."
        )

    return ipd


def update_ipd_service(
    db: Session,
    ipd_id: int,
    ipd_update: IPDUpdate,
    current_user: User,
):

    ipd = get_ipd_by_id(
        db,
        ipd_id,
    )

    if ipd is None:

        not_found(
            "IPD record not found."
        )

    update_data = ipd_update.model_dump(
        exclude_unset=True
    )

    if (
        "status" in update_data
        and update_data["status"] == "DISCHARGED"
    ):

        bed = get_bed_by_id(
            db,
            ipd.bed_id,
        )

        bed.status = "AVAILABLE"

        update_bed(
            db,
            bed,
        )

    for key, value in update_data.items():

        setattr(
            ipd,
            key,
            value,
        )

    updated = update_ipd(
        db,
        ipd,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="IPD",
        action="UPDATE",
    )

    return updated


def delete_ipd_service(
    db: Session,
    ipd_id: int,
    current_user: User,
):

    ipd = get_ipd_by_id(
        db,
        ipd_id,
    )

    if ipd is None:

        not_found(
            "IPD record not found."
        )

    if ipd.status == "ADMITTED":

        bed = get_bed_by_id(
            db,
            ipd.bed_id,
        )

        bed.status = "AVAILABLE"

        update_bed(
            db,
            bed,
        )

    delete_ipd(
        db,
        ipd,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="IPD",
        action="DELETE",
    )

    return {
        "message": "IPD record deleted successfully."
    }