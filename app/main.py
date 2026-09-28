from app.menu import Menu
from automations.example import ExampleAutomation
from core.registry import AutomationRegistry
from core.runner import AutomationRunner


def main():
    registry = AutomationRegistry()
    registry.register(ExampleAutomation())

    runner = AutomationRunner()
    menu = Menu(registry)

    while True:
        menu.display()

        choice = menu.get_choice()

        if choice == 0:
            print("\nEncerrando Python Switch Automate...")
            break

        automation = registry.get_all()[choice - 1]

        runner.run(automation)

        input("\nPressione Enter para voltar ao menu...")


if __name__ == "__main__":
    main()