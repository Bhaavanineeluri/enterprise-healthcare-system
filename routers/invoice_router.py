from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.invoice_schema import (
    InvoiceCreate,
    InvoiceResponse,
    InvoiceUpdate,
)

from services.invoice_service import (
    create_invoice_service,
    delete_invoice_service,
    get_all_invoices_service,
    get_invoice_service,
    update_invoice_service,
)


router = APIRouter(
    prefix="/invoices",
    tags=["Invoices"],
)


@router.post(
    "/",
    response_model=InvoiceResponse,
)
def create_invoice(
    invoice: InvoiceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_invoice_service(
        db=db,
        invoice=invoice,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[InvoiceResponse],
)
def get_all_invoices(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_invoices_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{invoice_id}",
    response_model=InvoiceResponse,
)
def get_invoice(
    invoice_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_invoice_service(
        db=db,
        invoice_id=invoice_id,
        current_user=current_user,
    )


@router.put(
    "/{invoice_id}",
    response_model=InvoiceResponse,
)
def update_invoice(
    invoice_id: int,
    invoice_update: InvoiceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_invoice_service(
        db=db,
        invoice_id=invoice_id,
        invoice_update=invoice_update,
        current_user=current_user,
    )


@router.delete(
    "/{invoice_id}",
)
def delete_invoice(
    invoice_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_invoice_service(
        db=db,
        invoice_id=invoice_id,
        current_user=current_user,
    )