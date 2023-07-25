from datetime import datetime

from pydantic import BaseModel
from enum import Enum
from typing import List, Optional


class ioc(BaseModel):
    indicator: str
    type:str
    severity:str
    expiration_date:Optional[str]
    comment:Optional[str]
    reputation:Optional[str]
    reliability:Optional[str]
    class_info:Optional[str] #for class
    vendor_name:Optional[str] #for_vendor.name
    vendor_reputation:Optional[str] #for vendor.reputation
    vendor_reliability:Optional[str] #for vendor.reliability
    validate: Optional[bool]



#Enum for naming

class indicator(Enum):
    indicator: str

class IndicatorType(Enum):
    hash = 'HASH'
    ip = 'IP'
    path = 'PATH'
    domain_name = 'DOMAIN_NAME'
    filename = 'FILENAME'


class Severity(Enum):
    info = 'informational'
    low = 'low'
    medium = 'medium'
    high = 'high'
    critical = 'critical'
    unknown = 'unknown'

class expirationDate(Enum):
    date = datetime

class comment(Enum):
    comment: str

class reliability(Enum):
    reliability: str

class IndicatorClass(Enum):
    indicatorClass = str

class vendorName(Enum):
    vendorName: str

class validate(Enum):
    validate = bool

class reputation(Enum):
    good = 'GOOD'
    bad = 'BAD'
    suspicious = 'SUSPICIOUS'
    unknown = 'UNKNOWN'












