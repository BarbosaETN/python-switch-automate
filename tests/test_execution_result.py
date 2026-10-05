from core.execution_result import ExecutionResult


def test_execution_result_success():
    result = ExecutionResult(
        automation_name="Teste",
        success=True,
        duration=1.25,
    )

    assert result.automation_name == "Teste"
    assert result.success is True
    assert result.duration == 1.25
    assert result.error is None

def test_execution_result_error():
    error = RuntimeError("Erro de teste.")

    result = ExecutionResult(
        automation_name="Teste",
        success=False,
        duration=0.50,
        error=error,
    )

    assert result.automation_name == "Teste"
    assert result.success is False
    assert result.duration == 0.50
    assert result.error is error    