from app.menu import Menu
from automations.example import ExampleAutomation
from core.registry import AutomationRegistry
from automations.register import register_automations
from automations.file_organizer import FileOrganizer


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

def test_menu_displays_file_organizer(capsys):
    registry = AutomationRegistry()

    register_automations(registry)

    menu = Menu(registry)

    menu.display()

    captured = capsys.readouterr()

    assert "Organizador de arquivos" in captured.out

def test_menu_selects_file_organizer(monkeypatch):
    registry = AutomationRegistry()

    register_automations(registry)

    monkeypatch.setattr("builtins.input", lambda _: "2")

    menu = Menu(registry)

    result = menu.get_selection()

    assert isinstance(result, FileOrganizer)

def test_file_organizer_can_be_selected_and_executed(monkeypatch, tmp_path):
    file = tmp_path / "documento.pdf"
    file.touch()

    inputs = iter(["2", str(tmp_path)])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    registry = AutomationRegistry()
    register_automations(registry)

    menu = Menu(registry)

    organizer = menu.get_selection()

    organizer.run()

    assert (tmp_path / "Documentos" / "documento.pdf").exists()               