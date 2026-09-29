from core.automation import Automation
from core.registry import AutomationRegistry


class Menu:
    def __init__(self, registry: AutomationRegistry):
        self.registry = registry

    def display(self) -> None:
        print("\n" + "=" * 40)
        print("       PYTHON SWITCH AUTOMATE")
        print("=" * 40)

        automations = self.registry.get_all()

        for index, automation in enumerate(automations, start=1):
            print(f"{index}. {automation.name}")

        print("0. Sair")

    def get_selection(self) -> Automation | None:
        while True:
            try:
                choice = int(input("\nEscolha uma opção: "))

                if choice == 0:
                    return None

                if 1 <= choice <= len(self.registry.get_all()):
                    return self.registry.get_by_index(choice - 1)

                print("Opção inválida.")

            except ValueError:
                print("Digite um número válido.")