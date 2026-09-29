from dataclasses import dataclass


@dataclass
class ExecutionResult:
    automation_name: str
    success: bool
    duration: float
    error: Exception | None = None