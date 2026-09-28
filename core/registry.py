from core.automation import Automation


class AutomationRegistry:
    def __init__(self):
        self._automations: list[Automation] = []

    def register(self, automation: Automation) -> None:
        self._automations.append(automation)

    def get_all(self) -> list[Automation]:
        return self._automations.copy()