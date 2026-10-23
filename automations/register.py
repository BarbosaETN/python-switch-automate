
from automations.example import ExampleAutomation
from core.registry import AutomationRegistry
from automations.file_organizer import FileOrganizer


def register_automations(registry: AutomationRegistry) -> None:
    registry.register(ExampleAutomation())
    registry.register(FileOrganizer())
