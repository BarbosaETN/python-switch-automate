import time

from core.automation import Automation
from core.execution_result import ExecutionResult


class AutomationRunner:
    def run(self, automation: Automation) -> ExecutionResult:
        print(f"\nExecutando: {automation.name}")

        start_time = time.perf_counter()

        try:
            automation.run()

            success = True
            error = None

        except Exception as exception:
            success = False
            error = exception

        duration = time.perf_counter() - start_time

        if success:
            print("\n✓ Automação concluída com sucesso.")
        else:
            print("\n✗ Ocorreu um erro durante a execução.")
            print(f"Erro: {error}")

        print(f"Tempo de execução: {duration:.2f}s")

        return ExecutionResult(
            automation_name=automation.name,
            success=success,
            duration=duration,
            error=error,
        )