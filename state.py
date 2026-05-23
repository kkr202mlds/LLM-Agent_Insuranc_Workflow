# Pydantic state models

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from enum import Enum

class AgentType(str, Enum):
    CLAIMS_TRIAGE = "claims_triage"
    POLICY_ISSUANCE = "policy_issuance"
    CUSTOMER_ONBOARDING = "customer_onboarding"
    DOCUMENT_PROCESSING = "document_processing"

class ClaimInfo(BaseModel):
    policy_number: Optional[str] = None
    incident_date: Optional[str] = None
    description: Optional[str] = None
    damage_estimate: Optional[float] = None
    urgency_score: Optional[float] = None  # 0-1

class PolicyDetails(BaseModel):
    customer_name: Optional[str] = None
    coverage_type: Optional[str] = None  # auto, home, life, etc.
    sum_insured: Optional[float] = None
    premium: Optional[float] = None
    risk_score: Optional[float] = None
    policy_document: Optional[str] = None  # generated text

class OnboardingData(BaseModel):
    customer_id: Optional[str] = None
    kyc_status: Optional[str] = None       # "verified", "pending"
    documents_required: List[str] = Field(default_factory=list)
    risk_profile: Optional[str] = None     # "low", "medium", "high"

class DocumentResult(BaseModel):
    doc_type: Optional[str] = None         # "claim_form", "id_proof", etc.
    extracted_text: Optional[str] = None
    confidence: Optional[float] = None

class InsuranceState(BaseModel):
    messages: List[Dict[str, Any]] = Field(default_factory=list)  # chat history
    current_agent: Optional[AgentType] = None
    claims: Optional[ClaimInfo] = None
    policy: Optional[PolicyDetails] = None
    onboarding: Optional[OnboardingData] = None
    document: Optional[DocumentResult] = None
    final_output: Optional[str] = None