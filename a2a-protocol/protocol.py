"""Simple in-memory message passing between agents."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List


@dataclass
class Message:
    sender: str
    receiver: str
    content: Any


_inbox: List[Message] = []


def send_message(msg: Message) -> None:
    """Place a message in the global inbox."""
    _inbox.append(msg)


def receive_messages(receiver: str) -> list[Message]:
    """Retrieve and clear messages for a receiver."""
    received = [m for m in _inbox if m.receiver == receiver]
    for m in received:
        _inbox.remove(m)
    return received
