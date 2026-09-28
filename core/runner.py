import time

from core.automation import Automation


class AutomationRunner:
    def run(self, automation: Automation) -> None:
        print(f"\nExecutando: {automation.name}")

        start_time = time.perf_counter()

        try:
            automation.run()
            print("\n✓ Automação concluída com sucesso.")

        except Exception as error:
            print("\n✗ Ocorreu um erro durante a execução.")
            print(f"Erro: {error}")

        finally:
            elapsed_time = time.perf_counter() - start_time
            print(f"Tempo de execução: {elapsed_time:.2f}s")