import pytest
from pathlib import Path

from automations.file_organizer import FileOrganizer


def test_get_category_for_document():
    organizer = FileOrganizer(Path("pasta_de_teste"))

    result = organizer.get_category(Path("arquivo.pdf"))

    assert result == "Documentos"


def test_get_category_for_image():
    organizer = FileOrganizer(Path("pasta_de_teste"))

    result = organizer.get_category(Path("foto.jpg"))

    assert result == "Imagens"


def test_get_category_for_audio():
    organizer = FileOrganizer(Path("pasta_de_teste"))

    result = organizer.get_category(Path("musica.mp3"))

    assert result == "Áudio"


def test_get_category_for_video():
    organizer = FileOrganizer(Path("pasta_de_teste"))

    result = organizer.get_category(Path("video.mp4"))

    assert result == "Vídeos"


def test_get_category_for_archive():
    organizer = FileOrganizer(Path("pasta_de_teste"))

    result = organizer.get_category(Path("arquivo.zip"))

    assert result == "Compactados"


def test_get_category_for_unknown_extension():
    organizer = FileOrganizer(Path("pasta_de_teste"))

    result = organizer.get_category(Path("arquivo.xyz"))

    assert result == "Outros"


def test_get_category_is_case_insensitive():
    organizer = FileOrganizer(Path("pasta_de_teste"))

    result = organizer.get_category(Path("FOTO.JPG"))

    assert result == "Imagens"

def test_organizer_stores_folder():
    folder = Path("pasta_de_teste")
    organizer = FileOrganizer(folder)

    assert organizer.folder == folder    

def test_validate_folder_with_valid_folder(tmp_path):
    organizer = FileOrganizer(tmp_path)

    organizer.validate_folder()

def test_validate_folder_when_folder_does_not_exist(tmp_path):
    folder = tmp_path / "nao_existe"
    organizer = FileOrganizer(folder)

    with pytest.raises(FileNotFoundError):
        organizer.validate_folder()

def test_validate_folder_when_path_is_file(tmp_path):
    file = tmp_path / "arquivo.txt"
    file.touch()

    organizer = FileOrganizer(file)

    with pytest.raises(NotADirectoryError):
        organizer.validate_folder()            