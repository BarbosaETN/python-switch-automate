
from automations.register import register_automations
from core.registry import AutomationRegistry


def test_register_automations():
    registry = AutomationRegistry()

    register_automations(registry)

    automations = registry.get_all()

    assert len(automations) == 2
    assert automations[0].name == "Automação de exemplo"
    assert automations[1].name == "Organizador de arquivos"
