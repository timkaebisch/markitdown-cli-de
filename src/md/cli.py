import sys
from pathlib import Path

from markitdown import MarkItDown


HELP = """
MarkItDown CLI
==============

Konvertiert Dokumente in Markdown.

VERWENDUNG

  md <datei>

      Konvertiert eine Datei und legt die .md-Datei
      im gleichen Ordner ab.

  md <datei1> <datei2> ...

      Konvertiert mehrere Dateien.

  md <ordner>

      Konvertiert alle unterstützten Dateien im Ordner.
      Unterordner werden nicht berücksichtigt.

BEISPIELE

  md document.pdf

      → document.md

  md document.pdf report.docx

      → document.md
      → report.md

  md *.pdf

      → konvertiert alle PDFs im aktuellen Ordner

  md ~/Documents/rechnungen

      → konvertiert alle unterstützten Dateien
        im Ordner "rechnungen"

UNTERSTÜTZTE FORMATE

  PDF, Word, PowerPoint, Excel, HTML,
  CSV, JSON, XML, TXT, EPUB und weitere.

HINWEIS

  Bereits vorhandene .md-Dateien werden beim Scannen
  eines Ordners ignoriert.

  Unterordner werden nicht durchsucht.

  Die erzeugten .md-Dateien werden immer im gleichen
  Ordner wie die Quelldateien gespeichert.

"""


SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".doc",
    ".pptx",
    ".ppt",
    ".xlsx",
    ".xls",
    ".html",
    ".htm",
    ".csv",
    ".json",
    ".xml",
    ".txt",
    ".epub",
}


def convert_file(converter, input_file):
    input_file = Path(input_file).expanduser().resolve()

    if not input_file.exists():
        print(f"❌ Nicht gefunden: {input_file}")
        return False

    if not input_file.is_file():
        print(f"❌ Keine Datei: {input_file}")
        return False

    output_file = input_file.with_suffix(".md")

    try:
        print(f"→ {input_file.name}")

        result = converter.convert(str(input_file))

        output_file.write_text(
            result.text_content,
            encoding="utf-8"
        )

        print(f"  ✓ {output_file.name}")
        return True

    except Exception as e:
        print(f"  ❌ Fehler: {e}")
        return False


def get_files_from_directory(directory):
    """Findet unterstützte Dateien direkt im angegebenen Ordner."""
    return sorted(
        file
        for file in directory.iterdir()
        if file.is_file()
        and file.suffix.lower() in SUPPORTED_EXTENSIONS
    )


def main():
    if len(sys.argv) == 1:
        print(HELP)
        return

    inputs = sys.argv[1:]
    files = []

    for input_path in inputs:
        path = Path(input_path).expanduser()

        if not path.exists():
            print(f"❌ Nicht gefunden: {path}")
            continue

        if path.is_dir():
            directory_files = get_files_from_directory(path)

            if not directory_files:
                print(f"⚠️ Keine unterstützten Dateien gefunden: {path}")
            else:
                print(
                    f"📁 {path.name}: "
                    f"{len(directory_files)} Datei(en) gefunden"
                )

            files.extend(directory_files)

        elif path.is_file():
            files.append(path)

        else:
            print(f"⚠️ Übersprungen: {path}")

    if not files:
        return

    converter = MarkItDown()

    success = 0
    failed = 0

    for file in files:
        if convert_file(converter, file):
            success += 1
        else:
            failed += 1

    if len(files) > 1:
        print()
        print(
            f"Fertig: {success} erfolgreich, "
            f"{failed} fehlgeschlagen."
        )


if __name__ == "__main__":
    main()
