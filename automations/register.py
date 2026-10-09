
from automations.example import ExampleAutomation
from core.registry import AutomationRegistry


def register_automations(registry: AutomationRegistry) -> None:
    registry.register(ExampleAutomation())
