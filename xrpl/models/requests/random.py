"""
The random command provides a random number to be
used as a source of entropy for random number generation by clients.
"""
from dataclasses import dataclass, field

from xrpl.models.requests.request import Request, RequestMethod


@dataclass(frozen=True)
class Random(Request):
    """
    The random command provides a random number to be
    used as a source of entropy for random number generation by clients.
    """

    method: RequestMethod = field(default=RequestMethod.RANDOM, init=False)
