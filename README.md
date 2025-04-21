# 📚 AI Study Assistant

An AI-powered personal study assistant built with Python.  
This tool extracts content from your PDF notes and YouTube videos, then generates:
- 📒 Notes
- 📌 Flashcards
- 📑 Formula Sheets
- ❓ Question Banks  

using OpenAI’s GPT model.

---

## 🎥 Demo Preview

*(You can add screenshots or GIFs here later if you want)*

---

## 📦 Features

✅ Extract text from PDF files  
✅ Extract transcript from YouTube videos  
✅ Generate study material using AI  
✅ Save generated content to text files  
✅ Clean menu-based interface  
✅ Completely local — your OpenAI API key stays private in your `.env` file

---

## 🛠️ Tech Stack

- Python
- OpenAI API
- PyPDF2
- youtube-transcript-api
- python-dotenv
- pytube

---

## 🚀 How to Run

1️⃣ Clone this repo:

```bash
git clone https://github.com/yourusername/ai-study-assistant.git
cd ai-study-assistant
```

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```
3️⃣ Create a .env file and add your OpenAI API key:

```ini
OPENAI_API_KEY=your-api-key-here
```
4️⃣ Run the app:

```bash
python main.py
```
📃 Project Structure

```arduino
ai-study-assistant/
├── .env
├── .gitignore
├── config.py
├── main.py
├── openai_prompt_handler.py
├── pdf_text_extractor.py
├── youtube_transcript_extractor.py
├── requirements.txt
└── README.md
```
📌 Roadmap
 AI-powered Notes, Flashcards, Formula Sheets & Question Banks

 Revision Booklet generator

 AI-based Topic Sorting

 Add GUI version with Tkinter / PyQt

 Docker support

📝 License
Free for personal and educational use.

🙌 Author
Haiqa Shahzad

⭐ Show some love by starring the repo if you find it useful!