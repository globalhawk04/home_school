### **README.md**

```markdown
# 📚 Homeschool Toolkit

A collection of custom Python scripts and tools designed to generate educational materials, worksheets, and resources for homeschooling.

## 🎯 Purpose

As a parent and developer, I wanted to create dynamic, printable resources tailored specifically to my children's current learning levels. This repository houses the code used to generate these materials automatically.

## 🛠️ Current Tools

### 1. Vocabulary Worksheet Generator (`vocab_builder.py`)
A script that helps children practice dictionary skills, reading, and handwriting.

*   **How it works:** 
    *   Contains a built-in database of **1,000+ words** ranging from easy sight words to complex academic vocabulary.
    *   Randomly selects 10 words every time the script is run.
    *   Generates a clean, printable `.html` file with the words and lined spaces for definitions.
    *   Automatically opens the worksheet in your default browser for immediate printing.
*   **Output:** `daily_vocab.html`

## 🚀 Getting Started

### Prerequisites
*   [Python 3.x](https://www.python.org/downloads/) installed on your machine.

### Installation
1.  Clone this repository:
    ```bash
    git clone https://github.com/your-username/homeschool-toolkit.git
    ```
2.  Navigate to the folder:
    ```bash
    cd homeschool-toolkit
    ```

### Usage
To generate a new Vocabulary Worksheet:

```bash
python vocab_builder.py
```
*The script will generate a file named `daily_vocab.html` in the same directory and attempt to open it automatically.*

## ⚙️ Customization

### Modifying the Word Bank
Open `vocab_builder.py` in any text editor. You will see a large list at the top:

```python
word_list = [
    "abundant", "adventure", "ancient", ...
]
```
*   **Add words:** Simply append new strings to the list: `"minecraft", "photosynthesis",`
*   **Remove words:** Delete any words that are too easy or not relevant.

### Adjusting Print Layout
If you need more space for writing definitions, look for this section in `vocab_builder.py`:

```html
<!-- Two lines for writing -->
<div class="definition-lines"></div>
<div class="definition-lines"></div>
```
Copy and paste the `<div class="definition-lines"></div>` line to add more writing space per word.

## 🔮 Future Ideas
*   Math problem generator (Addition/Subtraction/Multiplication).
*   Spelling test audio generator.
*   Reading log tracker.

## 📄 License
This project is open source and available for any parent to use!
```

***

### 💡 Pro Tip: Add a `.gitignore`
Since the script generates a `.html` file every time you run it, you probably don't want to save that specific HTML file to your GitHub history (since it changes every day).

Create a file named `.gitignore` in your folder and add this line to it:

```text
*.html
```

This tells GitHub, "Save my Python code, but ignore the temporary HTML files I generate."
