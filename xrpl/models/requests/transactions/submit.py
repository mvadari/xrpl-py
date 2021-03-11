"""
The submit method applies a transaction and sends it to the network to be confirmed and
included in future ledgers.

This command has two modes:
* Submit-only mode takes a signed, serialized transaction as a binary blob, and submits
it to the network as-is. Since signed transaction objects are immutable, no part of the
transaction can be modified or automatically filled in after submission.
* Sign-and-submit mode takes a JSON-formatted Transaction object, completes and signs
the transaction in the same manner as the sign method, and then submits the signed
transaction. We recommend only using this mode for testing and development.

To send a transaction as robustly as possible, you should construct and sign it in
advance, persist it somewhere that you can access even after a power outage, then
submit it as a tx_blob. After submission, monitor the network with the tx method
command to see if the transaction was successfully applied; if a restart or other
problem occurs, you can safely re-submit the tx_blob transaction: it won't be applied
twice since it has the same sequence number as the old transaction.

`See submit <https://xrpl.org/submit.html>`_
"""

from __future__ import annotations

from dataclasses import dataclass, field

from xrpl.models.requests.request import Request, RequestMethod


@dataclass(frozen=True)
class Submit(Request):
    """
    The submit method applies a transaction and sends it to the network to be confirmed
    and included in future ledgers.

    This command has two modes:
    * Submit-only mode takes a signed, serialized transaction as a binary blob, and
    submits it to the network as-is. Since signed transaction objects are immutable, no
    part of the transaction can be modified or automatically filled in after submission.
    * Sign-and-submit mode takes a JSON-formatted Transaction object, completes and
    signs the transaction in the same manner as the sign method, and then submits the
    signed transaction. We recommend only using this mode for testing and development.

    To send a transaction as robustly as possible, you should construct and sign it in
    advance, persist it somewhere that you can access even after a power outage, then
    submit it as a tx_blob. After submission, monitor the network with the tx method
    command to see if the transaction was successfully applied; if a restart or other
    problem occurs, you can safely re-submit the tx_blob transaction: it won't be
    applied twice since it has the same sequence number as the old transaction.

    `See submit <https://xrpl.org/submit.html>`_
    """

    method: RequestMethod = field(default=RequestMethod.SUBMIT, init=False)
