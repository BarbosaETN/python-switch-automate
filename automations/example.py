from core.automation import Automation


class ExampleAutomation(Automation):
    @property
    def name(self) -> str:
        return "Automação de exemplo"

    @property
    def description(self) -> str:
        return "Automação utilizada para testar o sistema."

    def run(self) -> None:
        print("\nExecutando automação de exemplo...")
        print("Automação executada com sucesso!")