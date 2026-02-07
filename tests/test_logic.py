import pytest
from app.main import xml_files_exist, ensure_directories

def test_get_xml_files(tmp_path, monkeypatch):
    # Arrange: create fake XML_DIR
    xml_dir = tmp_path / "xml"
    xml_dir.mkdir()

    (xml_dir / "Posts.xml").write_text("<posts />")
    (xml_dir / "Users.xml").write_text("<users />")
    (xml_dir / "README.txt").write_text("ignore me")
    (xml_dir / "votes.XML").write_text("<votes />")

    # Monkeypatch XML_DIR in the module under test
    monkeypatch.setattr(
        "app.main.XML_DIR",
        xml_dir
    )

    # Act
    files = xml_files_exist()

    # Assert
    filenames = sorted(p.name for p in files)
    assert filenames == ["Posts.xml", "Users.xml", "votes.XML"]