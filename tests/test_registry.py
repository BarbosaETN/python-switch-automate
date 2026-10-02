from automations.example import ExampleAutomation
from core.registry import AutomationRegistry


def test_register_automation():
    registry = AutomationRegistry()
    automation = ExampleAutomation()

    registry.register(automation)

    assert registry.get_by_index(0) is automation

def test_get_all_automations():
    registry = AutomationRegistry()
    automation = ExampleAutomation()

    registry.register(automation)

    automations = registry.get_all()

    assert len(automations) == 1
    assert automations[0] is automation