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

    def get_choice(self) -> int:
        while True:
            try:
                choice = int(input("\nEscolha uma opção: "))

                if 0 <= choice <= len(self.registry.get_all()):
                    return choice

                print("Opção inválida.")

            except ValueError:
                print("Digite um número válido.")