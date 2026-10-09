from automations.example import ExampleAutomation
from core.registry import AutomationRegistry
import pytest


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

def test_register_duplicate_automation():
    registry = AutomationRegistry()

    registry.register(ExampleAutomation())

    with pytest.raises(ValueError):
        registry.register(ExampleAutomation())


def test_get_by_name():
    registry = AutomationRegistry()
    automation = ExampleAutomation()
    registry.register(automation)

    result = registry.get_by_name("Automação de exemplo")

    assert result is automation


def test_get_by_name_returns_none_when_not_found():
    registry = AutomationRegistry()

    result = registry.get_by_name("Automação inexistente")

    assert result is None


def test_get_by_index_raises_error_for_invalid_index():
    registry = AutomationRegistry()
    registry.register(ExampleAutomation())

    with pytest.raises(IndexError, match="Não existe automação registrada"):
        registry.get_by_index(1)


def test_get_by_index_raises_error_for_negative_index():
    registry = AutomationRegistry()
    registry.register(ExampleAutomation())

    with pytest.raises(IndexError):
        registry.get_by_index(-1)
