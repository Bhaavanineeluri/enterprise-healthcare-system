from sqlalchemy.orm import Session

from core.exceptions import (
    not_found,
)

from models.lab_order import LabOrder
from models.user import User

from repositories.lab_order_repository import (
    create_lab_order,
    delete_lab_order,
    get_all_lab_orders,
    get_lab_order_by_id,
    get_lab_order_count,
    update_lab_order,
)

from repositories.emr_repository import (
    get_emr_by_id,
)

from repositories.patient_repository import (
    get_patient_by_id,
)

from repositories.doctor_repository import (
    get_doctor_by_id,
)

from schemas.lab_order_schema import (
    LabOrderCreate,
    LabOrderUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_lab_order_code(
    db: Session,
):

    count = get_lab_order_count(db)

    return f"LAB{count + 1:06d}"


def create_lab_order_service(
    db: Session,
    lab_order: LabOrderCreate,
    current_user: User,
):

    emr = get_emr_by_id(
        db,
        lab_order.emr_id,
    )

    if emr is None:

        not_found(
            "EMR not found."
        )

    patient = get_patient_by_id(
        db,
        lab_order.patient_id,
    )

    if patient is None:

        not_found(
            "Patient not found."
        )

    doctor = get_doctor_by_id(
        db,
        lab_order.doctor_id,
    )

    if doctor is None:

        not_found(
            "Doctor not found."
        )

    new_lab_order = LabOrder(

        lab_order_code=generate_lab_order_code(
            db,
        ),

        emr_id=lab_order.emr_id,

        patient_id=lab_order.patient_id,

        doctor_id=lab_order.doctor_id,

        test_name=lab_order.test_name,

        test_category=lab_order.test_category,

        priority=lab_order.priority,

        clinical_notes=lab_order.clinical_notes,

        order_date=lab_order.order_date,

        status="ORDERED",
    )

    lab_order_data = create_lab_order(
        db,
        new_lab_order,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="LAB_ORDER",
        action="CREATE",
    )

    return lab_order_data


def get_all_lab_orders_service(
    db: Session,
    current_user: User,
):

    return get_all_lab_orders(
        db,
    )
    
def get_lab_order_service(
    db: Session,
    lab_order_id: int,
    current_user: User,
):

    lab_order = get_lab_order_by_id(
        db,
        lab_order_id,
    )

    if lab_order is None:

        not_found(
            "Lab Order not found."
        )

    return lab_order


def update_lab_order_service(
    db: Session,
    lab_order_id: int,
    lab_order_update: LabOrderUpdate,
    current_user: User,
):

    lab_order = get_lab_order_by_id(
        db,
        lab_order_id,
    )

    if lab_order is None:

        not_found(
            "Lab Order not found."
        )

    update_data = lab_order_update.model_dump(
        exclude_unset=True,
    )

    for key, value in update_data.items():

        setattr(
            lab_order,
            key,
            value,
        )

    updated = update_lab_order(
        db,
        lab_order,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="LAB_ORDER",
        action="UPDATE",
    )

    return updated


def delete_lab_order_service(
    db: Session,
    lab_order_id: int,
    current_user: User,
):

    lab_order = get_lab_order_by_id(
        db,
        lab_order_id,
    )

    if lab_order is None:

        not_found(
            "Lab Order not found."
        )

    delete_lab_order(
        db,
        lab_order,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="LAB_ORDER",
        action="DELETE",
    )

    return {
        "message": "Lab Order deleted successfully."
    }