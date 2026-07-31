from sqlalchemy.orm import Session

from core.exceptions import (
    not_found,
)

from models.treatment_plan import TreatmentPlan
from models.user import User

from repositories.treatment_plan_repository import (
    create_treatment_plan,
    delete_treatment_plan,
    get_all_treatment_plans,
    get_treatment_plan_by_id,
    get_treatment_plan_count,
    update_treatment_plan,
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

from schemas.treatment_plan_schema import (
    TreatmentPlanCreate,
    TreatmentPlanUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_treatment_plan_code(
    db: Session,
):

    count = get_treatment_plan_count(db)

    return f"TP{count + 1:06d}"


def create_treatment_plan_service(
    db: Session,
    treatment_plan: TreatmentPlanCreate,
    current_user: User,
):

    emr = get_emr_by_id(
        db,
        treatment_plan.emr_id,
    )

    if emr is None:

        not_found(
            "EMR not found."
        )

    patient = get_patient_by_id(
        db,
        treatment_plan.patient_id,
    )

    if patient is None:

        not_found(
            "Patient not found."
        )

    doctor = get_doctor_by_id(
        db,
        treatment_plan.doctor_id,
    )

    if doctor is None:

        not_found(
            "Doctor not found."
        )

    new_treatment_plan = TreatmentPlan(

        treatment_plan_code=generate_treatment_plan_code(
            db
        ),

        emr_id=treatment_plan.emr_id,

        patient_id=treatment_plan.patient_id,

        doctor_id=treatment_plan.doctor_id,

        treatment_title=treatment_plan.treatment_title,

        treatment_description=treatment_plan.treatment_description,

        treatment_goals=treatment_plan.treatment_goals,

        follow_up_plan=treatment_plan.follow_up_plan,

        status="ACTIVE",
    )

    treatment_plan_data = create_treatment_plan(
        db,
        new_treatment_plan,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="TREATMENT_PLAN",
        action="CREATE",
    )

    return treatment_plan_data


def get_all_treatment_plans_service(
    db: Session,
    current_user: User,
):

    return get_all_treatment_plans(
        db
    )


def get_treatment_plan_service(
    db: Session,
    treatment_plan_id: int,
    current_user: User,
):

    treatment_plan = get_treatment_plan_by_id(
        db,
        treatment_plan_id,
    )

    if treatment_plan is None:

        not_found(
            "Treatment Plan not found."
        )

    return treatment_plan


def update_treatment_plan_service(
    db: Session,
    treatment_plan_id: int,
    treatment_plan_update: TreatmentPlanUpdate,
    current_user: User,
):

    treatment_plan = get_treatment_plan_by_id(
        db,
        treatment_plan_id,
    )

    if treatment_plan is None:

        not_found(
            "Treatment Plan not found."
        )

    update_data = treatment_plan_update.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():

        setattr(
            treatment_plan,
            key,
            value,
        )

    updated = update_treatment_plan(
        db,
        treatment_plan,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="TREATMENT_PLAN",
        action="UPDATE",
    )

    return updated


def delete_treatment_plan_service(
    db: Session,
    treatment_plan_id: int,
    current_user: User,
):

    treatment_plan = get_treatment_plan_by_id(
        db,
        treatment_plan_id,
    )

    if treatment_plan is None:

        not_found(
            "Treatment Plan not found."
        )

    delete_treatment_plan(
        db,
        treatment_plan,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="TREATMENT_PLAN",
        action="DELETE",
    )

    return {
        "message": "Treatment Plan deleted successfully."
    }