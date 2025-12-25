# PC Building Chatbot

A dual-mode chatbot that helps users build desktop PCs with specific recommendations across different budgets and use cases.

## Features

### 🖥️ Local Chatbot (Pattern-Based)
- **Budget-based recommendations**: Specific PC builds from $500 to $3000+
- **Multiple use cases**: Gaming, Workstation, and Streaming builds
- **Intelligent budget extraction**: Automatically detects budget amounts from queries
- **Component guidance**: CPU, GPU, and RAM recommendations
- **No internet required**: Works completely offline

### 🤖 AI Chatbot (OpenRouter)
- Powered by OpenAI GPT-3.5-turbo via OpenRouter
- Conversational AI with context awareness
- Requires API key and internet connection

---

## Requirements

### System Requirements
- **Python**: 3.7 or higher
- **Operating System**: Windows, macOS, or Linux

### Dependencies

#### For Local Chatbot (Pattern-Based)
**No external dependencies required!** Uses only Python standard library:
- `json` (built-in)
- `random` (built-in)
- `re` (built-in)

#### For AI Chatbot (OpenRouter)
- `openai` library (version 1.0.0 or higher)

---

## Installation

### 1. Install Python
Download and install Python from [python.org](https://www.python.org/downloads/)

### 2. Clone/Download the Project
Copy these files to your new PC:
- `local_chatbot.py`
- `chatbot.py`
- `intents.json`
- `requirements.txt` (optional, only for AI mode)

### 3. Install Dependencies (Optional - Only for AI Chatbot)

If you want to use the **AI chatbot mode**, install the required library:

```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install openai
```

**Note**: The local chatbot works without any installations!

---

## Usage

### Running the Chatbot

#### Option 1: Main Menu (Both Modes)
```bash
python chatbot.py
```
Choose between:
1. Local Chatbot (Pattern-based, no setup needed)
2. AI Chatbot (Requires OpenRouter API key)

#### Option 2: Local Chatbot Only
```bash
python local_chatbot.py
```

### Example Queries for Local Chatbot

**Budget-based queries:**
- `gaming pc for $1000`
- `workstation 1500`
- `build for 600`
- `streaming pc 2000`

**Component queries:**
- `what gpu should i get`
- `what cpu should i get`
- `how much ram do i need`

**General queries:**
- `help me build a pc`
- `1440p gaming build`
- `video editing pc 1200`

---

## Configuration

### For AI Chatbot Mode
Edit `chatbot.py` and replace the API key on line 26:
```python
MY_OPENROUTER_KEY = "your-api-key-here"
```

Get your API key from [OpenRouter](https://openrouter.ai/)

---

## Project Structure

```
chatbot terminal/
├── chatbot.py           # Main entry point with mode selection
├── local_chatbot.py     # Local pattern-matching chatbot
├── intents.json         # PC build recommendations database
├── requirements.txt     # Python dependencies (for AI mode)
└── README.md           # This file
```

---

## Build Recommendations Included

### Gaming Builds
- **Entry ($500-700)**: 1080p gaming, 60+ fps
- **Mid-Range ($900-1200)**: 1440p gaming, 100+ fps
- **High-End ($1500-1800)**: 4K gaming, 60+ fps
- **Enthusiast ($2000-3000)**: 4K ultra, 100+ fps

### Workstation Builds
- **Entry ($500-700)**: Programming, office work
- **Mid-Range ($1000-1500)**: Video editing, 3D modeling
- **High-End ($2000-3000)**: Professional rendering, VMs

### Streaming Build
- **$1500-2000**: Stream + game simultaneously

---

## Troubleshooting

### "Module not found" error
- Make sure Python is installed: `python --version`
- For AI mode, install dependencies: `pip install openai`

### Local chatbot not responding correctly
- Ensure `intents.json` is in the same directory as `local_chatbot.py`

### Unicode/encoding errors
- Already fixed in the current version (removed emojis for Windows compatibility)

---

## License

Free to use and modify for personal and educational purposes.

---

## Support

For issues or questions, check that:
1. Python 3.7+ is installed
2. All files are in the same directory
3. For AI mode: `openai` library is installed
4. For AI mode: Valid OpenRouter API key is configured
