from dataclasses import dataclass, field

@dataclass(order=True, unsafe_hash=True)
class Student:
    id: int
    name: str = field(compare=False)
    score: int = field(compare=False)