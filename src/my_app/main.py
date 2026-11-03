"""Application entry point."""

from __future__ import annotations


def greet(name: str = "world") -> str:
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
