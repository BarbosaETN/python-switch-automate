from pathlib import Path

from core.automation import Automation


class FileOrganizer(Automation):
    CATEGORIES = {
        "Documentos": {".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"},
        "Imagens": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"},
        "Áudio": {".mp3", ".wav", ".flac", ".aac", ".ogg"},
        "Vídeos": {".mp4", ".avi", ".mkv", ".mov", ".wmv"},
        "Compactados": {".zip", ".rar", ".7z", ".tar", ".gz"},
    }

    def __init__(self, folder: Path):
        self.folder = folder

    @property
    def name(self) -> str:
        return "Organizador de arquivos"

    @property
    def description(self) -> str:
        return "Organiza arquivos de uma pasta por tipo."

    def get_category(self, file: Path) -> str:
        extension = file.suffix.lower()

        for category, extensions in self.CATEGORIES.items():
            if extension in extensions:
                return category

        return "Outros"

    def validate_folder(self) -> None:
        if not self.folder.exists():
            raise FileNotFoundError(
                f"A pasta '{self.folder}' não existe."
            )

        if not self.folder.is_dir():
            raise NotADirectoryError(
                f"O caminho '{self.folder}' não é uma pasta."
            )

    def run(self) -> None:
        pass