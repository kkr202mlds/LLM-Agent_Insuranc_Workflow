# Mock insurance tools (OCR, risk, KYC, etc.)

import random
import time
from typing import Optional

# ---------- Document Processing Tools ----------
def ocr_extract_text(document_type: str, file_path: str = "dummy.png") -> str:
    """Simulate OCR extraction based on document type."""
    templates = {
        "claim_form": "Policy: POL-1234, Incident: 2025-01-15 car accident, Damage: $4500",
        "id_proof": "Name: John Doe, DOB: 1990-05-20, ID: A1234567",
        "medical_report": "Diagnosis: whiplash, treatment cost: $1200",
        "police_report": "Report #PR-889, accident confirmed, fault: other party"
    }
    return templates.get(document_type, "No text extracted")

def classify_document(text: str) -> str:
    """Mock document classifier."""
    text_lower = text.lower()
    if "policy" in text_lower and "claim" in text_lower:
        return "claim_form"
    elif "name" in text_lower and "dob" in text_lower:
        return "id_proof"
    elif "diagnosis" in text_lower or "treatment" in text_lower:
        return "medical_report"
    elif "police" in text_lower or "report #" in text_lower:
        return "police_report"
    return "unknown"

# ---------- Claims Triage Tools ----------
def assess_claim_urgency(description: str, damage_estimate: float) -> float:
    """Simple rule-based urgency score (mock)."""
    keywords_urgent = ["hospital", "total loss", "fire", "flood", "theft", "injury"]
    score = 0.3
    for kw in keywords_urgent:
        if kw in description.lower():
            score += 0.15
    if damage_estimate > 50000:
        score += 0.2
    return min(score, 1.0)

def lookup_policy(policy_number: str) -> Optional[dict]:
    """Mock policy DB lookup."""
    db = {
        "POL-1234": {"status": "active", "coverage": "auto", "deductible": 500},
        "POL-5678": {"status": "active", "coverage": "home", "deductible": 1000},
    }
    return db.get(policy_number)

# ---------- Policy Issuance Tools ----------
def calculate_risk_score(customer_data: dict) -> float:
    """Mock underwriting risk engine."""
    base = 0.2
    if customer_data.get("age", 30) < 25:
        base += 0.3
    if customer_data.get("credit_score", 700) < 600:
        base += 0.2
    if customer_data.get("claims_history", 0) > 2:
        base += 0.2
    return min(base, 0.95)

def generate_policy_document(customer_name: str, coverage_type: str, sum_insured: float, premium: float) -> str:
    """Mock policy document generation."""
    return f"""
POLICY DOCUMENT
================
Insured: {customer_name}
Type: {coverage_type} Insurance
Sum Insured: ${sum_insured:,.2f}
Annual Premium: ${premium:,.2f}
Effective Date: 2026-06-01
Policy Number: POL-{random.randint(10000,99999)}
Terms: Standard terms apply.
"""

# ---------- Customer Onboarding Tools ----------
def perform_kyc_check(customer_id: str) -> dict:
    """Mock KYC check."""
    # Simulate 80% pass rate
    passed = random.random() > 0.2
    return {"status": "verified" if passed else "pending", "missing_docs": [] if passed else ["proof_of_address"]}

def required_documents_for_product(product: str) -> list:
    """Return list of required onboarding documents."""
    mapping = {
        "auto": ["driver_license", "vehicle_registration", "previous_insurance"],
        "home": ["property_deed", "id_proof", "valuation_report"],
        "life": ["id_proof", "medical_exam", "income_proof"]
    }
    return mapping.get(product, ["id_proof", "address_proof"])