# 🗂️ File Sorter Automation

A Python-based file organizer that automatically sorts files into folders based on file extensions using configurations from a JSON file.

## ⚙️ Features
- Reads config.json for flexible setup.
- Creates missing destination folders automatically.
- Handles duplicate filenames gracefully.
- Logs all operations to `file_sorter.log`.

## 🧾 Example Config
```json
{
  "Target_Directory": "C:/Users/Karna/Downloads",
  "Destination_Directories": {
    "Images": "C:/Users/Karna/Downloads/Images",
    "Documents": "C:/Users/Karna/Downloads/Documents",
    "Others": "C:/Users/Karna/Downloads/Others"
  },
  "File_Types": {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Others": []
  }
}
```

## Run
```bash
python file_sorter.py
```

## Author

Karnan G