# Datathon App

This repository contains a full-stack application with a Next.js frontend and a FastAPI backend.

## Prerequisites

- Node.js and npm (for the frontend)
- Python 3.8+ (for the backend)
- Git

## How to Clone the Repository

To clone the app to your local machine, open your terminal and run:

```bash
git clone <repository-url>
cd datathon
```
*(Note: Replace `<repository-url>` with the actual URL of your git repository)*

## Running the Application Locally

The application is split into two parts: the client (frontend) and the server (backend). You will need to run both concurrently in separate terminal windows.

### 1. Start the Backend Server (FastAPI)

Open a terminal and navigate to the `server` directory:

```bash
cd server
```

If you haven't already, activate the virtual environment and install the required dependencies:

```bash
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate

# Install dependencies (if you have a requirements.txt, run pip install -r requirements.txt)
pip install fastapi uvicorn
```

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

The server will start running on `http://localhost:8000`. You can check if it's running by visiting `http://localhost:8000/`.

### 2. Start the Frontend Client (Next.js)

Open a **new** terminal window and navigate to the `client` directory:

```bash
cd client
```

Install the Node dependencies (only required the first time):

```bash
npm install
```

Start the Next.js development server:

```bash
npm run dev
```

The frontend will start running on `http://localhost:3000`. Open this URL in your browser to view the app.
