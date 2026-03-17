from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class StartResolutionMessage:
    organization_name: str
    address: str


@dataclass
class NormalizedAddressMessage:
    organization_name: str
    original_address: str
    normalized_address: str


@dataclass
class RegistryLookupMessage:
    organization_name: str
    normalized_address: str
    registry_result: Dict[str, Any]


@dataclass
class ResolutionResultMessage:
    result: Dict[str, Any]
