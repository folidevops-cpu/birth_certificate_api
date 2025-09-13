from pydantic import BaseModel
from datetime import date
from typing import Optional

class ParentInformation(BaseModel):
    name: str
    nationality: str
    profession: str
    residence: str
    date_of_birth: Optional[date]
    place_of_birth: str

class ChildInformation(BaseModel):
    name: str
    date_of_birth: Optional[date]
    place_of_birth: str
    sex: str

class CertificateInformation(BaseModel):
    title: str
    registration_number: str
    date_of_issue: date
    issuing_authority: str
    registrar_name: str

class BirthCertificate(BaseModel):
    certificate_info: CertificateInformation
    child_info: ChildInformation
    father_info: ParentInformation
    mother_info: ParentInformation