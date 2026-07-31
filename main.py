from fastapi import FastAPI

from config.settings import settings


from middleware.security_headers import SecurityHeadersMiddleware
from routers.auth_router import router as auth_router
from routers.user_router import router as user_router
from routers.hospital_router import router as hospital_router
from routers.hospital_router import router as hospital_router
from routers.branch_router import router as branch_router
from routers.department_router import router as department_router
from routers.doctor_router import router as doctor_router
from routers.staff_router import router as staff_router
from routers.patient_router import (router as patient_router)
from routers.ward_router import (router as ward_router)
from routers.room_router import (router as room_router)
from routers.bed_router import (router as bed_router)
from routers.emergency_router import (router as emergency_router)
from routers.ambulance_router import (router as ambulance_router)
from routers.appointment_router import (router as appointment_router)
from routers.opd_router import (router as opd_router)
from routers.ipd_router import (router as ipd_router)
from routers.emr_router import (router as emr_router)
from routers.diagnosis_router import (router as diagnosis_router)
from routers.prescription_router import (router as prescription_router)
from routers.treatment_plan_router import router as treatment_plan_router
from routers.clinical_note_router import (router as clinical_note_router)
from routers.surgery_router import (router as surgery_router)
from routers.discharge_summary_router import (router as discharge_summary_router)
from routers.lab_order_router import (router as lab_order_router)
from routers.sample_collection_router import (router as sample_collection_router)
from routers.test_processing_router import (router as test_processing_router)
from routers.result_publishing_router import (router as result_publishing_router)
from routers.pharmacy_inventory_router import (router as pharmacy_inventory_router)
from routers.prescription_validation_router import (router as prescription_validation_router)
from routers.medicine_dispensing_router import (router as medicine_dispensing_router)
from routers.drug_stock_management_router import (router as drug_stock_management_router)
from routers.batch_tracking_router import (router as batch_tracking_router)
from routers.expiry_management_router import (router as expiry_management_router)
from routers.billing_router import (router as billing_router)
from routers.invoice_router import (router as invoice_router)
from routers.payment_router import (router as payment_router)
from routers.insurance_claim_router import (router as insurance_claim_router)
from routers.refund_router import (router as refund_router)
from routers.revenue_report_router import (router as revenue_report_router)
from routers.financial_report_router import (router as financial_report_router)
from routers.tax_calculation_router import (router as tax_calculation_router)
from routers.audit_report_router import (router as audit_report_router)
from routers.document_router import (router as document_router)
from routers.notification_router import (router as notification_router)
from routers.workflow_router import (router as workflow_router)
from routers.ocr_router import (router as ocr_router)
from routers.search_router import (router as search_router)
from routers.dashboard_router import (router as dashboard_router)
from routers.reporting_engine_router import (router as reporting_engine_router)
from routers.background_task_router import (router as background_task_router)
from routers.cache_router import (router as cache_router)
from routers.monitoring_router import (router as monitoring_router)

             























app = FastAPI(
    title="Enterprise Healthcare System",
    version="1.0.0",
    description="Enterprise Healthcare Information System Backend API",
)






app.add_middleware(SecurityHeadersMiddleware)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(hospital_router)
app.include_router(hospital_router)
app.include_router(branch_router)
app.include_router(department_router)
app.include_router(doctor_router)
app.include_router(staff_router)
app.include_router(patient_router)
app.include_router(ward_router)
app.include_router(room_router)
app.include_router(bed_router)
app.include_router(emergency_router)
app.include_router(ambulance_router)
app.include_router(appointment_router)
app.include_router(opd_router)
app.include_router(ipd_router)
app.include_router(emr_router)
app.include_router(diagnosis_router)
app.include_router(prescription_router)
app.include_router(treatment_plan_router)
app.include_router(clinical_note_router)
app.include_router(surgery_router)
app.include_router(discharge_summary_router)
app.include_router(lab_order_router)
app.include_router(sample_collection_router)
app.include_router(test_processing_router)
app.include_router(result_publishing_router)
app.include_router(pharmacy_inventory_router)
app.include_router(prescription_validation_router)
app.include_router(medicine_dispensing_router)
app.include_router(drug_stock_management_router)
app.include_router(batch_tracking_router)
app.include_router(expiry_management_router)
app.include_router(billing_router)
app.include_router(invoice_router)
app.include_router(payment_router)
app.include_router(insurance_claim_router)
app.include_router(refund_router)
app.include_router(revenue_report_router)
app.include_router(financial_report_router)
app.include_router(tax_calculation_router)
app.include_router(audit_report_router)
app.include_router(document_router)
app.include_router(notification_router)
app.include_router(workflow_router)
app.include_router(ocr_router)
app.include_router(search_router)
app.include_router(dashboard_router)
app.include_router(reporting_engine_router)
app.include_router(background_task_router)
app.include_router(cache_router)
app.include_router(monitoring_router)




@app.get("/")
def home():
    return {
        "message": settings.APP_NAME
    }