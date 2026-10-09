
from core.automation import Automation


class AutomationRegistry:
    def __init__(self):
        self._automations: list[Automation] = []

    def register(self, automation: Automation) -> None:
        if any(
            registered.name == automation.name
            for registered in self._automations
        ):
            raise ValueError(
                f"A automação '{automation.name}' já está registrada."
            )

        self._automations.append(automation)

    def get_all(self) -> list[Automation]:
        return self._automations.copy()

        
    def get_by_index(self, index: int) -> Automation:
        if not 0 <= index < len(self._automations):
            raise IndexError(
                f"Não existe automação registrada no índice {index}."
            )

        return self._automations[index]

    
    def get_by_name(self, name: str) -> Automation | None:
        for automation in self._automations:
            if automation.name == name:
                return automation

        return None
