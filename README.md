# Gemmio

> **Gemmio** — bring Google Gemini into your terminal. Fast, minimal, and forkable. 🌱🩸

## Short description

Gemmio is a lightweight, open-source Python terminal client that lets you interact with Google Gemini directly from your command line. It’s built to be forked and customized: users paste their own Gemini API key into the `API_KEY` variable and run `gemmio.py`. The project includes a striking dot-based ASCII logo colored in **blood-red** and **green**, a simple chat loop, and clear instructions so anyone can get started quickly.

---

## ASCII Logo (terminal-ready)

```
··········································
····███████····███····███····
····██······██···██··██···██··
····███████···██····██···██··
····██······██···██···██···██··
····███████····███····███····
··········································
```

*(In the shipped script the logo prints colored using `colorama` — red for background dots and green for the blocks.)*

---

## Features

* Terminal-first chat client for Google Gemini (via `google-generativeai`).
* Minimal single-file entrypoint (`gemmio.py`) — easy to read and fork.
* Clear placeholder API key so users know where to replace it: `AIzaSyAvW4wShWmzlLtExZnyRDCkPTg2-bfdhlc` (replace with your own).
* Colorful dot-based ASCII logo (blood-red + green).
* Friendly error messages and an easy `exit` flow.

---

## Requirements

* Python 3.10+ (recommended)
* `pip` for installing dependencies
* A Google Gemini API key (place it in `gemmio.py`)

---

## Installation

1. Clone this repo:

```bash
git clone https://github.com/yourusername/gemmio.git
cd gemmio
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate    # Windows (PowerShell)
```

3. Install dependencies:

```bash
pip install -r requirements.txt
# or
pip install google-generativeai colorama
```

---

## Configuration

Open `gemmio.py` and locate the `API_KEY` variable near the top. Replace the sample placeholder with your own Google Gemini API key:

```python
API_KEY = "AIzaSyAvW4wShWmzlLtExZnyRDCkPTg2-bfdhlc"  # replace this with your key
```

> **Important:** The included sample key is only a placeholder. Do not commit personal/secret keys to public repositories. Instead, for public forks, add a `.env` or use environment variables if you want to keep keys secret.

---

## Usage

Run Gemmio from the terminal:

```bash
python gemmio.py
```

Type a message and press Enter. Type `exit` or `quit` to leave.

---

## Troubleshooting

* **`[ERROR] Please replace the sample API key`** — you forgot to update `API_KEY`.
* **ImportError** — ensure you installed `google-generativeai` and `colorama` in the active environment.
* **API errors / auth failures** — double-check the Gemini API key, its permissions, and whether the model name (`gemini-1.5-flash`) is available to your account.

---

## Contributing

You’re encouraged to fork and extend Gemmio. Ideas:

* Add environment variable support (`python-dotenv` or `os.environ`).
* Add history saving, command flags, or a `--model` override.
* Add streaming responses for long outputs.
* Provide packaging (`pip install gemmio`) and CI for linting/tests.

When contributing:

1. Fork the repo.
2. Create a feature branch.
3. Open a PR with a clear description of changes.

---

## LICENSE

This project is provided under the **MIT License**. See the LICENSE block below for the full text.

---

# LICENSE (MIT)

MIT License

Copyright (c) 2025 Soham

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

Thank you for building Gemmio. If you want, I can also:

* Create a ready `requirements.txt` and `.gitignore`.
* Produce a polished `gemmio.py` file (complete single-file starter) inside the repo.
* Generate a short logo image for the repo README (PNG/SVG).

