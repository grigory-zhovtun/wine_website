"""
Simple HTTP server using Jinja2 to generate a page with wine data.

This module performs the following actions:
1. Render an HTML template with wine data.
2. Write the generated page to the file index.html.
3. Start an HTTP server to serve the generated page.
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

from utils.get_wines_data import get_wines_data


def render_template() -> None:
    """
    Render an HTML template with wine data and write it to the file index.html.

    Jinja2 is used to load the template from the 'templates' directory.
    The 'years' parameter is set to the string "103", and wine data is
    retrieved using the get_wines_data function.
    """
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    wines = get_wines_data()
    rendered_page = template.render(
        years="103",
        wines=wines,
    )

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)


def run_server(host: str = '0.0.0.0', port: int = 8000) -> None:
    """
    Start an HTTP server on the specified host and port.

    Args:
        host: The IP address for the server to listen on. Default is '0.0.0.0'.
        port: The port to run the server on. Default is 8000.
    """
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()


def main() -> None:
    """
    Generate the page and start the server.

    Steps:
    1. Render the HTML template with wine data.
    2. Write the result to the file index.html.
    3. Start the HTTP server to serve the generated page.
    """
    render_template()
    run_server()


if __name__ == '__main__':
    main()
