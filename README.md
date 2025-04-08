# Wine Store Web Application

This Python project generates a dynamic web page displaying categorized wine data using Jinja2 templates. It also serves the page via a simple HTTP server.

---

## Features

- Retrieves wine data from an Excel file.
- Categorizes and structures the wine data dynamically.
- Generates an HTML page using Jinja2 templates.
- Serves the web page via a built-in HTTP server.

---

## Prerequisites

- Python 3.6 or later
- Required dependencies specified in `requirements.txt`

---

## Installation and Setup

1. **Clone the repository or download the project files:**

   ```bash
   git clone https://github.com/yourusername/wine-store.git
   cd wine-store
   ```

2. **(Optional) Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux/macOS
   venv\Scripts\activate          # Windows
   ```

3. **Install dependencies from **``**:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure the Excel file **``** is placed in the **``** directory.**

---

## Environment Variables Setup

The application uses the following environment variables:

•	**EXCEL_FILE_PATH**: Path to excel file with wines data.

Make sure to create a .env file in the project root and define these variables accordingly before running the program.
---

## Usage

### Running the Web Server

```bash
python main.py
```

This will:

- Render the `template.html` page with wine data.
- Save the generated page as `index.html`.
- Start an HTTP server to serve the page.

You can then access the web page at:
[http://127.0.0.1:8000](http://127.0.0.1:8000)


### Updating Wine Data

If the Excel file (`wine3.xlsx`) is modified, restart the server to refresh the data:

```bash
python main.py
```

---

## Dependencies

This project requires the following Python libraries:

- `http.server` (built-in)
- `jinja2`
- `pandas`
- `openpyxl`

To install them, run:

```bash
pip install -r requirements.txt
```

---

## Customization

- Modify `template.html` to change the UI.
- Update `get_wines_data.py` to process additional wine attributes.
- Adjust `main.py` to add more server functionalities.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.