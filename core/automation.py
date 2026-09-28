from abc import ABC, abstractmethod


class Automation(ABC):
    """Base class for all Switch Automate automations."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the automation name."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Return the automation description."""
        pass

    @abstractmethod
    def run(self) -> None:
        """Execute the automation."""
        pass