# FastAPI Echo Server

This is a simple FastAPI application that serves an HTML form for echoing back user messages.

## Features

- A web page with a form where users can enter a message.
- A `/echo` endpoint that receives a JSON payload and returns it back to the client.
- Logging to track the requests and responses.

## Running the Server

1. **Start the server:**
    ```sh
    python -m uvicorn main:app --reload
    ```
![image](https://github.com/AMARNATH2470/Adapt/assets/97387420/d6d7aa73-6c31-4011-8e0e-43cf7e0a9485)

2. **Open your browser and navigate to `http://127.0.0.1:8000/` to see the form.**

![image](https://github.com/AMARNATH2470/Adapt/assets/97387420/7066acc2-9553-412b-b9c9-f69ca2b0457a)

## Endpoints

### GET /

Serves the HTML form for echoing messages.

### POST /echo

Receives a JSON payload and returns it back to the client.

**Request Body:**
```json
{
  "message": "Message will be printed here"
}
