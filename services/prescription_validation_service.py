from datetime import date

from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.prescription_validation import PrescriptionValidation
from models.user import User

from repositories.pharmacy_inventory_repository import (
    get_pharmacy_inventory_by_id,
)

from repositories.prescription_repository import (
    get_prescription_by_id,
)

from repositories.prescription_validation_repository import (
    create_prescription_validation,
    delete_prescription_validation,
    get_all_prescription_validations,
    get_prescription_validation_by_id,
    get_prescription_validation_count,
    update_prescription_validation,
)

from schemas.prescription_validation_schema import (
    PrescriptionValidationCreate,
    PrescriptionValidationUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_validation_code(
    db: Session,
):

    count = get_prescription_validation_count(db)

    return f"PVAL{count + 1:06d}"


def create_prescription_validation_service(
    db: Session,
    validation: PrescriptionValidationCreate,
    current_user: User,
):

    prescription = get_prescription_by_id(
        db,
        validation.prescription_id,
    )

    if prescription is None:

        not_found(
            "Prescription not found."
        )

    inventory = get_pharmacy_inventory_by_id(
        db,
        validation.pharmacy_inventory_id,
    )

    if inventory is None:

        not_found(
            "Medicine not found in inventory."
        )

    if inventory.status != "AVAILABLE":

        bad_request(
            "Medicine is not available."
        )

    if inventory.expiry_date <= date.today():

        bad_request(
            "Medicine batch has expired."
        )

    if inventory.quantity < validation.requested_quantity:

        bad_request(
            "Insufficient stock available."
        )

    if validation.approved_quantity > validation.requested_quantity:

        bad_request(
            "Approved quantity cannot exceed requested quantity."
        )

    new_validation = PrescriptionValidation(

        validation_code=generate_validation_code(
            db,
        ),

        prescription_id=validation.prescription_id,

        pharmacy_inventory_id=validation.pharmacy_inventory_id,

        requested_quantity=validation.requested_quantity,

        approved_quantity=validation.approved_quantity,

        validation_status="VALIDATED",

        remarks=validation.remarks,

        validated_by=validation.validated_by,

        validation_date=validation.validation_date,
    )

    validation_data = create_prescription_validation(
        db,
        new_validation,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="PRESCRIPTION_VALIDATION",
        action="CREATE",
    )

    return validation_data


def get_all_prescription_validations_service(
    db: Session,
    current_user: User,
):

    return get_all_prescription_validations(
        db,
    )


def get_prescription_validation_service(
    db: Session,
    validation_id: int,
    current_user: User,
):

    validation = get_prescription_validation_by_id(
        db,
        validation_id,
    )

    if validation is None:

        not_found(
            "Prescription Validation not found."
        )

    return validation


def update_prescription_validation_service(
    db: Session,
    validation_id: int,
    validation_update: PrescriptionValidationUpdate,
    current_user: User,
):

    validation = get_prescription_validation_by_id(
        db,
        validation_id,
    )

    if validation is None:

        not_found(
            "Prescription Validation not found."
        )

    update_data = validation_update.model_dump(
        exclude_unset=True,
    )

    for key, value in update_data.items():

        setattr(
            validation,
            key,
            value,
        )

    updated = update_prescription_validation(
        db,
        validation,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="PRESCRIPTION_VALIDATION",
        action="UPDATE",
    )

    return updated


def delete_prescription_validation_service(
    db: Session,
    validation_id: int,
    current_user: User,
):

    validation = get_prescription_validation_by_id(
        db,
        validation_id,
    )

    if validation is None:

        not_found(
            "Prescription Validation not found."
        )

    delete_prescription_validation(
        db,
        validation,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="PRESCRIPTION_VALIDATION",
        action="DELETE",
    )

    return {
        "message": "Prescription Validation deleted successfully."
    }