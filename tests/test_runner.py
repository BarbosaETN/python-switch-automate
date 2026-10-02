from automations.example import ExampleAutomation
from core.automation import Automation
from core.runner import AutomationRunner


class FailingAutomation(Automation):
    @property
    def name(self) -> str:
        return "Automação com erro"

    @property
    def description(self) -> str:
        return "Automação utilizada para testar erros."

    def run(self) -> None:
        raise RuntimeError("Erro de teste.")


def test_runner_success():
    runner = AutomationRunner()
    automation = ExampleAutomation()

    result = runner.run(automation)

    assert result.success is True
    assert result.error is None
    assert result.automation_name == automation.name


def test_runner_records_duration():
    runner = AutomationRunner()
    automation = ExampleAutomation()

    result = runner.run(automation)

    assert result.duration >= 0


def test_runner_handles_error():
    runner = AutomationRunner()
    automation = FailingAutomation()

    result = runner.run(automation)

    assert result.success is False
    assert isinstance(result.error, RuntimeError)
    assert str(result.error) == "Erro de teste."