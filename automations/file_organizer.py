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

    def __init__(self, folder: Path | None = None):
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

    def get_files(self) -> list[Path]:
        self.validate_folder()

        return [
            item
            for item in self.folder.iterdir()
            if item.is_file()
        ]

    def create_category_folder(self, category: str) -> Path:
        category_folder = self.folder / category
        category_folder.mkdir(exist_ok=True)

        return category_folder

    def get_unique_destination(self, destination: Path, filename: str) -> Path:
        target = destination / filename

        if not target.exists():
            return target

        file = Path(filename)
        counter = 1

        while True:
            new_name = f"{file.stem} ({counter}){file.suffix}"
            target = destination / new_name

            if not target.exists():
                return target

            counter += 1    

    def move_file(self, file: Path, destination: Path) -> Path:
        target = self.get_unique_destination(destination, file.name)
        file.rename(target)

        return target   

    def run(self) -> None:
        if self.folder is None:
            folder_input = input("Digite o caminho da pasta: ")
            self.folder = Path(folder_input)

        files = self.get_files()

        organized_count = 0

        for file in files:
            category = self.get_category(file)
            destination = self.create_category_folder(category)
            self.move_file(file, destination)
            organized_count += 1

        print(f"{organized_count} arquivos organizados com sucesso.")