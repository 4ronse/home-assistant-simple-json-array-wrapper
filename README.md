# Simple HTTP Server Addon for Home Assistant

This addon runs a simple HTTP server with one endpoint (/fetch) that fetches a JSON array from a given URL and wraps it in a JSON object.

## Usage

After installing the addon, you can make GET requests to:

`http://your-home-assistant:8000/fetch?url=<your-json-url>`

The server will fetch the JSON from the provided URL, wrap it in a "data" object, and return the result.
