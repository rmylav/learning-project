# learning-project

A simple terminal tool that lets you ask Claude questions and get answers, right from the command line. Built as a first hands-on project for learning how to work with the Anthropic API.

## What it does

- Prompts you for a question
- Sends it to Claude via the Anthropic API
- Prints the response
- Loops so you can keep asking questions until you type `quit`
- Handles errors gracefully (shows a clear message instead of crashing)

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/rmylav/learning-project.git
cd learning-project
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a `.env` file in the project root:

```
ANTHROPIC_API_KEY=your-api-key-here
```

You can get an API key from [console.anthropic.com](https://console.anthropic.com).

> The `.env` file is gitignored and should never be committed.

## Usage

```bash
python3 ask.py
```

Type a question when prompted. Type `quit` to exit.

## Tech stack

- Python 3
- [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python)
- `python-dotenv` for loading the API key from `.env`

## Status

This is a learning project, built step by step to understand the basics of calling an LLM API: request/response handling, looping, environment variables, and error handling. It's intentionally simple — a starting point rather than a finished product.
