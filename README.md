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
*   **Output:** `daily_vocab.html`

### 2. Math Worksheet Generator (`math.py`)
A dynamic worksheet creator for Addition, Subtraction, Multiplication, and Division.

*   **How it works:**
    *   Asks the user for the **number of problems** and **difficulty level**.
    *   **Smart Logic:** Ensures subtraction results are never negative and division results are always whole numbers.
    *   **Visual Aids:** "Easy" mode automatically generates dot counters (visuals) to help young learners count.
    *   **Print-Ready:** Creates a two-column layout with a "Name" and "Date" header, optimized for black-and-white printing.
*   **Difficulty Levels:**
    *   *Easy:* Numbers 1–10 (with visuals).
    *   *Medium:* Numbers 10–100.
    *   *Hard:* Numbers 100–1,000.
*   **Output:** `math_worksheet.html`

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

**To generate a Vocabulary Worksheet:**
```bash
python vocab_builder.py

To generate a Math Worksheet:

code
Bash
download
content_copy
expand_less
python math.py

Follow the on-screen prompts to select difficulty and problem count. The script will generate a file named math_worksheet.html and open it automatically.

⚙️ Customization
Modifying the Vocabulary List

Open vocab_builder.py in any text editor. You will see a large list at the top:

code
Python
download
content_copy
expand_less
word_list = [
    "abundant", "adventure", "ancient", ...
]

Simply add or remove words from this list to tailor it to your child's grade level.

Modifying Math Ranges

Open math.py and look for the generate_problems function. You can manually adjust the number ranges for specific difficulties:

code
Python
download
content_copy
expand_less
if difficulty == 'medium':
    num_min, num_max = 10, 100 # Change these numbers to adjust range
🔮 Future Ideas

Spelling test audio generator.
Reading log tracker.
Geography quiz generator.

This project is open source and available for any parent to use!
