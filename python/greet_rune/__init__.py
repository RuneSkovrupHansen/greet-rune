from .greet_rune import greet as greet_rust

def greet_py() -> None:
    print("Hi Rune!")

__all__ = ["greet_py", "greet_rust"]
