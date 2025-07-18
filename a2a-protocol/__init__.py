"""Agent-to-Agent communication primitives."""

from .protocol import Message, send_message

__all__ = ["Message", "send_message"]
