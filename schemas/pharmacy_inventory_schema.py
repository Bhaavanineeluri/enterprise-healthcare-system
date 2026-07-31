from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class PharmacyInventoryCreate(BaseModel):

    medicine_name: str

    generic_name: Optional[str] = None

    manufacturer: Optional[str] = None

    dosage_form: str

    strength: str

    batch_number: str

    expiry_date: date

    quantity: int

    minimum_stock: int = 10

    unit_price: Decimal

    storage_location: Optional[str] = None


class PharmacyInventoryUpdate(BaseModel):

    medicine_name: Optional[str] = None

    generic_name: Optional[str] = None

    manufacturer: Optional[str] = None

    dosage_form: Optional[str] = None

    strength: Optional[str] = None

    batch_number: Optional[str] = None

    expiry_date: Optional[date] = None

    quantity: Optional[int] = None

    minimum_stock: Optional[int] = None

    unit_price: Optional[Decimal] = None

    storage_location: Optional[str] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class PharmacyInventoryResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    pharmacy_inventory_code: str

    medicine_name: str

    generic_name: Optional[str]

    manufacturer: Optional[str]

    dosage_form: str

    strength: str

    batch_number: str

    expiry_date: date

    quantity: int

    minimum_stock: int

    unit_price: Decimal

    storage_location: Optional[str]

    status: str

    is_active: bool