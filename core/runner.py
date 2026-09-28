from core.automation import Automation


class AutomationRunner:
    def run(self, automation: Automation) -> None:
        print(f"\nExecutando: {automation.name}")

        try:
            automation.run()
            print("\n✓ Automação concluída com sucesso.")

        except Exception as error:
            print("\n✗ Ocorreu um erro durante a execução.")
            print(f"Erro: {error}")