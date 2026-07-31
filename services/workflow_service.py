from models.user import User

from schemas.workflow_schema import (
    WorkflowRequest,
)


def execute_workflow_service(
    workflow: WorkflowRequest,
    current_user: User,
):

    """
    Future workflows:

    PATIENT_REGISTRATION

    APPOINTMENT_BOOKING

    LAB_RESULT

    INSURANCE_APPROVAL

    PATIENT_DISCHARGE

    BILL_GENERATION
    """

    return {

        "success": True,

        "workflow": workflow.workflow_name,

        "message":
            f"{workflow.workflow_name} executed successfully.",
    }