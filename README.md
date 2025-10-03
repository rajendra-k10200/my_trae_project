# Trae Projects

This project contains a simple chatbot application that uses the Google Gemini API.

## Project Structure

- `llm_app.py`: The main entry point for the chatbot application.
- `main.py`: A secondary entry point.
- `requirements.txt`: A list of Python dependencies for the project.
- `.env`: A file to store environment variables, such as your Google API key.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/trae-projects.git
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Create a `.env` file:**
   Create a `.env` file in the root of the project and add your Google API key:
   ```
   GOOGLE_API_KEY=your-api-key
   ```

## Usage

To run the chatbot, execute the following command:

```bash
python llm_app.py
```

This will start an interactive chat session in your terminal. Type "exit" to end the conversation.
