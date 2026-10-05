from app.menu import Menu
from automations.example import ExampleAutomation
from core.registry import AutomationRegistry


def create_menu():
    registry = AutomationRegistry()
    automation = ExampleAutomation()

    registry.register(automation)

    return Menu(registry), automation

def test_get_selection_returns_selected_automation(monkeypatch):
    menu, automation = create_menu()

    monkeypatch.setattr("builtins.input", lambda _: "1")

    result = menu.get_selection()

    assert result is automation

def test_get_selection_returns_none_when_user_exits(monkeypatch):
    menu, _ = create_menu()

    monkeypatch.setattr("builtins.input", lambda _: "0")

    result = menu.get_selection()

    assert result is None

def test_get_selection_rejects_invalid_option(monkeypatch):
    menu, automation = create_menu()

    inputs = iter(["99", "1"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = menu.get_selection()

    assert result is automation

def test_get_selection_rejects_non_numeric_input(monkeypatch):
    menu, automation = create_menu()

    inputs = iter(["abc", "1"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = menu.get_selection()

    assert result is automation            