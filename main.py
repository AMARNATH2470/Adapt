from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import logging
import json

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/echo")
async def echo(request: Request):
    """
    Endpoint to echo back the received JSON message.
    """
    logger.info('1')  
    data = await request.json()  
    logger.info(f"Received /echo request with message: {data}")  
    return data  

@app.get("/", response_class=HTMLResponse)
async def read_root():
    logger.info('2')
    """
    Endpoint to serve the main HTML page with the echo form.
    """
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI Echo Server</title>
    </head>
    <body>
        <h1>Welcome to the FastAPI Echo Server</h1>
        <form id="echoForm">
            <label for="message">Message:</label>
            <input type="text" id="message" name="message">
            <button type="submit">Send</button>
        </form>
        <h2>Response:</h2>
        <pre id="response"></pre>
        <script>
            document.getElementById('echoForm').addEventListener('submit', async function(event) {
                event.preventDefault();  // Prevent the form from submitting the default way
                const message = document.getElementById('message').value;  // Get the message from the input field
                const response = await fetch('/echo', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ message })  // Send the message as JSON
                });
                const responseData = await response.json();  // Wait for and parse the JSON response
                document.getElementById('response').textContent = JSON.stringify(responseData, null, 2);  // Display the response on the page
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)  
