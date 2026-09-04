# MarkItDown CLI

Ein kleines CLI-Tool für macOS, das [Microsoft MarkItDown](https://github.com/microsoft/markitdown) verwendet, um Dokumente in Markdown-Dateien umzuwandeln.

## Installation

### 1. Repository klonen

Öffne das Terminal und führe aus:

```bash
git clone https://github.com/timkaebisch/markitdown-cli-de.git ~/.markitdown
```

Danach liegt das Projekt unter:

```text
~/.markitdown
```

---

### 2. Python-Version prüfen

MarkItDown benötigt **Python 3.10 oder neuer**.

Prüfe deine Python-Version:

```bash
python3 --version
```

Beispiel:

```text
Python 3.14.0
```

Falls deine Version **älter als 3.10** ist, kannst du Python mit Homebrew installieren bzw. aktualisieren:

```bash
brew install python
```

Danach erneut prüfen:

```bash
python3 --version
```

Falls `python3` weiterhin eine alte Version anzeigt, kann es sein, dass dein macOS noch eine andere Python-Installation verwendet.

Prüfe in diesem Fall:

```bash
which -a python3
```

---

### 3. pipx installieren

`pipx` kümmert sich automatisch um die isolierte Python-Umgebung für das CLI.

Prüfe zunächst:

```bash
pipx --version
```

Falls `pipx` noch nicht installiert ist:

```bash
brew install pipx
```

Danach:

```bash
pipx ensurepath
```

Anschließend das Terminal einmal **schließen und neu öffnen**.

Prüfe erneut:

```bash
pipx --version
```

---

### 4. MarkItDown CLI installieren

Wechsle in das geklonte Repository:

```bash
cd ~/.markitdown
```

Installiere das CLI mit:

```bash
pipx install .
```

Damit wird das Kommando `md` global verfügbar gemacht.

Prüfe die Installation:

```bash
md
```

Wenn alles funktioniert, wird die Hilfe des Programms angezeigt.

---

# Verwendung

## Eine Datei konvertieren

```bash
md document.pdf
```

Die Markdown-Datei wird automatisch im gleichen Ordner erstellt:

```text
document.pdf
document.md
```

Das funktioniert beispielsweise auch mit:

```bash
md document.docx
md presentation.pptx
md spreadsheet.xlsx
```

---

## Mehrere Dateien konvertieren

Mehrere Dateien können gleichzeitig angegeben werden:

```bash
md document.pdf report.docx presentation.pptx
```

Für jede Datei wird eine entsprechende `.md`-Datei im gleichen Ordner erstellt.

---

## Mehrere Dateien mit Wildcards

Auf macOS kannst du beispielsweise alle PDFs im aktuellen Ordner konvertieren:

```bash
md *.pdf
```

Oder alle Word-Dateien:

```bash
md *.docx
```

---

## Einen kompletten Ordner konvertieren

Du kannst auch einen Ordner angeben:

```bash
md ~/Documents/rechnungen
```

Das CLI sucht nach unterstützten Dateien **direkt in diesem Ordner** und konvertiert sie.

Unterordner werden aktuell **nicht** durchsucht.

Beispiel:

```text
rechnungen/
├── januar.pdf
├── februar.pdf
├── maerz.docx
├── bereits.md
└── unterordner/
    └── april.pdf
```

Bei:

```bash
md ~/Documents/rechnungen
```

werden konvertiert:

```text
januar.pdf
februar.pdf
maerz.docx
```

`bereits.md` wird ignoriert und `unterordner/april.pdf` wird nicht berücksichtigt.

---

# Hilfe anzeigen

Wenn du `md` ohne Argumente ausführst:

```bash
md
```

wird die integrierte Hilfe angezeigt.

Sie enthält die verfügbaren Befehle, Beispiele und Hinweise zur Verwendung.

---

# Ausgabe

Die erzeugten Markdown-Dateien werden immer neben der ursprünglichen Datei abgelegt.

Beispiel:

```text
Documents/
└── projekt/
    ├── bericht.pdf
    └── bericht.md
```

Der Dateiname bleibt gleich, nur die Dateiendung wird zu `.md`.

---

# Aktualisieren

Wenn das Repository aktualisiert wurde:

```bash
cd ~/.markitdown
git pull
```

Danach das CLI neu installieren:

```bash
pipx install --force .
```

Damit wird die lokal installierte Version aktualisiert.

---

# Deinstallation

Um das CLI wieder zu entfernen:

```bash
pipx uninstall markitdown-cli
```

Das Repository unter `~/.markitdown` bleibt dabei erhalten.

Falls du auch das Repository löschen möchtest:

```bash
rm -rf ~/.markitdown
```

> **Achtung:** Dadurch wird das komplette Projektverzeichnis gelöscht.

---

# Voraussetzungen

* macOS
* Python **3.10 oder neuer**
* Homebrew (für die einfache Installation von Python und pipx)
* Git
* pipx

## Kurzfassung

Für eine neue Installation:

```bash
git clone <link> ~/.markitdown
brew install python
brew install pipx
pipx ensurepath
```

Terminal neu öffnen und anschließend:

```bash
cd ~/.markitdown
pipx install .
```

Danach:

```bash
md document.pdf
```

oder:

```bash
md ~/Documents/meine-dokumente
```

Fertig.
