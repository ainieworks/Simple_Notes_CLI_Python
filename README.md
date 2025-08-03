# 📝 Simple Notes CLI (Python)

A clean and beginner-friendly **command-line Notes Manager** built using Python and JSON.  
It lets you **add**, **view**, and **delete** notes with timestamps — stored persistently in a `data.json` file.

---

## 🚀 Features

- 📌 Add new notes with title, content, and current timestamp  
- 📂 View all saved notes in a formatted list  
- ❌ Delete any note by its number  
- 📅 Human-readable date and time formatting  
- 🧠 Graceful handling of corrupted or empty JSON  
- ⚙️ Fully written in Python with no third-party libraries

---

## 🔧 How It Works

Each note is saved as an object in a `data.json` file:

```json
{
  "title": "Study Plan",
  "content": "Complete CLI project by Sunday",
  "timestamp": "2025-08-03 11:45:00.123456"
}
The app automatically loads existing notes and updates them based on your commands.

🛠 Usage
Run the script using:

bash
Copy
Edit
python main.py
Follow the on-screen menu to:

Add note

View notes

Delete note

Exit

📂 File Structure
bash
Copy
Edit
main.py       # Main application logic  
data.json     # Stores all notes  
💡 Inspiration
This project was part of my personal practice building Python CLI tools with file handling and logic control — including real-world features like date formatting, validation, and user experience polish.

👩‍💻 Author
Qurat Ul Ain (@ainieworks)

