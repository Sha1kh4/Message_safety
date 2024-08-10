# Message_safety

## Overview

This project is a simple web application built with Flask and Flask-SocketIO. It allows users to send and receive messages in real-time using WebSockets. The application also includes logging to help track and debug message handling.

## Features

- **Real-time Messaging:** Send and receive messages using Socket.IO.
- **Encrypted Messaging:** Support for encrypted messages (currently just handled as regular messages).
- **Logging:** Detailed logging to both the console and a file for debugging and monitoring.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Sha1kh4/Message_safety.git
    cd Message_safety
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:
    
      ```bash
      venv\Scripts\activate
      ```
      
    - On macOS/Linux:
    
      ```bash
      source venv/bin/activate
      ```

4. **Install the required packages:**

    ```bash
    pip install flask flask-socketio
    ```

## Usage

1. **Run the application:**

    ```bash
    python app.py
    ```

2. **Open your web browser and navigate to:**

    - [Welcome Page](http://127.0.0.1:5000/)
    - [Chat Page](http://127.0.0.1:5000/chat)

3. **To send messages:**
    - Go to the chat page and use the interface to send messages.
    - Messages are broadcasted to all connected clients.

## Code Overview

- **app.py:** Contains the Flask application setup, routes, and Socket.IO event handlers.
  - **Logging Configuration:** Configures logging to output messages to both the console and a file (`app.log`).
  - **Routes:**
    - `/`: Renders the `welcome.html` template.
    - `/chat`: Renders the `index.html` template for the chat interface.
  - **Socket.IO Event Handlers:**
    - `send_message`: Receives messages and broadcasts them to all clients.
    - `send_encrypted_message`: Similar to `send_message`, but intended for encrypted messages (currently treated as regular messages).

## Logging

Logging is set up to capture detailed information about message events:

- **Log Level:** DEBUG
- **Log File:** `app.log`
- **Console Logging:** Enabled via `StreamHandler`
- **File Logging:** Enabled via `FileHandler`

## Templates

- **welcome.html:** A simple welcome page
- **index.html:** The main chat interface
