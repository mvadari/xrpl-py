"""Collection of public constants for XRPL."""
import re
from enum import Enum
from typing import Pattern

from typing_extensions import Final


class CryptoAlgorithm(str, Enum):
    """Represents the supported cryptography algorithms."""

    ED25519 = "ed25519"
    SECP256K1 = "secp256k1"


class XRPLException(Exception):
    """Base Exception for XRPL library."""

    pass


ISO_CURRENCY_REGEX: Final[Pattern[str]] = re.compile("[A-Z0-9]{3}")
"""
Matches ISO currencies like "USD" or "EUR" in the format allowed by XRPL.

:meta private:
"""

HEX_CURRENCY_REGEX: Final[Pattern[str]] = re.compile("[A-F0-9]{40}")
"""
Matches hex-encoded currencies in the format allowed by XRPL.

:meta private:
"""
