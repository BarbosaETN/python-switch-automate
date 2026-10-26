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

def test_get_files_returns_files(tmp_path):
    file_1 = tmp_path / "arquivo.txt"
    file_2 = tmp_path / "foto.jpg"

    file_1.touch()
    file_2.touch()

    organizer = FileOrganizer(tmp_path)

    result = organizer.get_files()

    assert len(result) == 2
    assert file_1 in result
    assert file_2 in result

def test_get_files_ignores_directories(tmp_path):
    file = tmp_path / "arquivo.txt"
    directory = tmp_path / "outra_pasta"

    file.touch()
    directory.mkdir()

    organizer = FileOrganizer(tmp_path)

    result = organizer.get_files()

    assert result == [file]

def test_get_files_returns_empty_list_for_empty_folder(tmp_path):
    organizer = FileOrganizer(tmp_path)

    result = organizer.get_files()

    assert result == []

def test_create_category_folder(tmp_path):
    organizer = FileOrganizer(tmp_path)

    result = organizer.create_category_folder("Imagens")

    assert result == tmp_path / "Imagens"
    assert result.exists()
    assert result.is_dir()

def test_create_existing_category_folder(tmp_path):
    organizer = FileOrganizer(tmp_path)

    organizer.create_category_folder("Imagens")
    result = organizer.create_category_folder("Imagens")

    assert result.exists()
    assert result.is_dir()

def test_move_file(tmp_path):
    source = tmp_path / "foto.jpg"
    destination = tmp_path / "Imagens"

    source.touch()
    destination.mkdir()

    organizer = FileOrganizer(tmp_path)

    result = organizer.move_file(source, destination)

    assert result == destination / "foto.jpg"
    assert not source.exists()
    assert result.exists()

def test_run_organizes_files(tmp_path):
    document = tmp_path / "documento.pdf"
    image = tmp_path / "foto.jpg"
    audio = tmp_path / "musica.mp3"

    document.touch()
    image.touch()
    audio.touch()

    organizer = FileOrganizer(tmp_path)

    organizer.run()

    assert (tmp_path / "Documentos" / "documento.pdf").exists()
    assert (tmp_path / "Imagens" / "foto.jpg").exists()
    assert (tmp_path / "Áudio" / "musica.mp3").exists()

    assert not document.exists()
    assert not image.exists()
    assert not audio.exists()

def test_get_unique_destination_when_file_does_not_exist(tmp_path):
    organizer = FileOrganizer(tmp_path)

    result = organizer.get_unique_destination(
        tmp_path,
        "foto.jpg"
    )

    assert result == tmp_path / "foto.jpg"

def test_get_unique_destination_when_file_already_exists(tmp_path):
    existing_file = tmp_path / "foto.jpg"
    existing_file.touch()

    organizer = FileOrganizer(tmp_path)

    result = organizer.get_unique_destination(
        tmp_path,
        "foto.jpg"
    )

    assert result == tmp_path / "foto (1).jpg"

def test_get_unique_destination_skips_existing_names(tmp_path):
    (tmp_path / "foto.jpg").touch()
    (tmp_path / "foto (1).jpg").touch()
    (tmp_path / "foto (2).jpg").touch()

    organizer = FileOrganizer(tmp_path)

    result = organizer.get_unique_destination(
        tmp_path,
        "foto.jpg"
    )

    assert result == tmp_path / "foto (3).jpg"

def test_move_file_with_duplicate_name(tmp_path):
    source = tmp_path / "foto.jpg"
    destination = tmp_path / "Imagens"

    source.touch()
    destination.mkdir()

    existing_file = destination / "foto.jpg"
    existing_file.touch()

    organizer = FileOrganizer(tmp_path)

    result = organizer.move_file(source, destination)

    assert result == destination / "foto (1).jpg"
    assert result.exists()
    assert existing_file.exists()
    assert not source.exists()

def test_run_does_not_overwrite_duplicate_file(tmp_path):
    source = tmp_path / "foto.jpg"
    source.touch()

    images_folder = tmp_path / "Imagens"
    images_folder.mkdir()

    existing_file = images_folder / "foto.jpg"
    existing_file.touch()

    organizer = FileOrganizer(tmp_path)

    organizer.run()

    assert existing_file.exists()
    assert (images_folder / "foto (1).jpg").exists()
    assert not source.exists()

def test_organizer_can_be_created_without_folder():
    organizer = FileOrganizer()

    assert organizer.folder is None

def test_run_asks_for_folder_when_not_provided(monkeypatch, tmp_path):
    monkeypatch.setattr("builtins.input", lambda _: str(tmp_path))

    organizer = FileOrganizer()

    organizer.run()

    assert organizer.folder == tmp_path

def test_run_raises_error_for_invalid_folder(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "C:\\pasta-que-nao-existe"
    )

    organizer = FileOrganizer()

    with pytest.raises(FileNotFoundError):
        organizer.run()

def test_run_displays_number_of_organized_files(tmp_path, capsys):
    document = tmp_path / "documento.pdf"
    image = tmp_path / "foto.jpg"

    document.touch()
    image.touch()

    organizer = FileOrganizer(tmp_path)

    organizer.run()

    captured = capsys.readouterr()

    assert "2 arquivos organizados" in captured.out    