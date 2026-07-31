from sqlalchemy.orm import Session

from models.treatment_plan import TreatmentPlan


def create_treatment_plan(
    db: Session,
    treatment_plan: TreatmentPlan,
):

    db.add(treatment_plan)

    db.commit()

    db.refresh(treatment_plan)

    return treatment_plan


def get_all_treatment_plans(
    db: Session,
):

    return (

        db.query(TreatmentPlan)

        .filter(
            TreatmentPlan.is_active == True
        )

        .all()

    )


def get_treatment_plan_by_id(
    db: Session,
    treatment_plan_id: int,
):

    return (

        db.query(TreatmentPlan)

        .filter(
            TreatmentPlan.id == treatment_plan_id
        )

        .first()

    )


def get_treatment_plan_count(
    db: Session,
):

    return db.query(TreatmentPlan).count()


def update_treatment_plan(
    db: Session,
    treatment_plan: TreatmentPlan,
):

    db.commit()

    db.refresh(treatment_plan)

    return treatment_plan


def delete_treatment_plan(
    db: Session,
    treatment_plan: TreatmentPlan,
):

    treatment_plan.is_active = False

    db.commit()

    db.refresh(treatment_plan)

    return treatment_plan