# AI Exam Paper Analyzer

##  Project Overview

AI Exam Paper Analyzer is a Python-based web application that analyzes exam paper images.

The application allows the user to upload an exam paper image. It uses **Tesseract OCR** to extract text from the image and then analyzes the extracted text to identify questions, classify them into Easy, Medium, and Hard categories, and detect the total marks.

The application is built using **Streamlit**, **Pytesseract**, **Pillow**, and Python **Regular Expressions (Regex)**.

> Note: The current version uses rule-based text analysis for question classification. It does not use a trained machine-learning or deep-learning model.

---

##  Objectives

The main objectives of this project are:

* Upload an exam paper as an image.
* Extract text automatically using OCR.
* Clean the extracted OCR text.
* Detect questions from the exam paper.
* Remove question numbers and unnecessary headings.
* Identify Easy, Medium, and Hard questions.
* Detect total marks from common mark formats.
* Display all extracted questions.
* Provide a simple web interface using Streamlit.

---

##  Features

### 1. Exam Paper Upload

Users can upload exam paper images in:

* PNG
* JPG
* JPEG

### 2. OCR Text Extraction

The application uses Tesseract OCR to convert the exam paper image into machine-readable text.

### 3. Text Cleaning

The extracted OCR text is cleaned by:

* Removing unnecessary spaces.
* Removing extra blank lines.
* Fixing selected OCR mistakes.
* Converting carriage returns into new lines.

### 4. Question Detection

The application detects questions using:

* Numbered questions such as `1.` and `2)`
* Roman numerals such as `(i)` and `(ii)`
* Question words such as:

  * What is
  * What are
  * Define
  * Explain
  * Discuss
  * Describe
  * Write
  * List
  * Identify
  * How
  * Why

### 5. Difficulty Classification

Questions are classified into three categories:

*  Easy
*  Medium
*  Hard

The current classification is based on keywords.

#### Easy keywords

```text
what is
what are
define
list
write a short note
```

#### Hard keywords

```text
explain
discuss
compare
describe
analyze
evaluate
```

Questions that do not match the Easy or Hard keywords are classified as Medium.

### 6. Total Marks Detection

The application can detect mark patterns such as:

```text
5 x 2 = 10
3 x 10 = 30
```

It extracts the values and calculates the total.

### 7. Analysis Report

The application displays:

* Total number of questions
* Number of Easy questions
* Number of Medium questions
* Number of Hard questions
* Total marks
* Easy questions
* Medium questions
* Hard questions
* All detected questions

---

##  Technologies Used

| Technology          | Purpose                                 |
| ------------------- | --------------------------------------- |
| Python              | Main programming language               |
| Streamlit           | Web application interface               |
| Tesseract OCR       | Extract text from exam paper images     |
| Pytesseract         | Python interface for Tesseract OCR      |
| Pillow              | Image processing and opening images     |
| Regular Expressions | Pattern matching and question detection |

---

##  Project Structure

```text
AI-Exam-Paper-Analyzer/
│
├── app.py
├── ocr.py
├── analyzer.py
├── requirements.txt
└── README.md
```

### `app.py`

Contains the Streamlit application.

It handles:

* File upload
* Image display
* Analyze button
* OCR processing
* Displaying extracted text
* Displaying final analysis

### `ocr.py`

Contains the OCR functionality.

It:

1. Opens the uploaded image.
2. Sends the image to Tesseract.
3. Extracts the text.
4. Returns the extracted text.

### `analyzer.py`

Contains the main text-analysis logic.

It handles:

* OCR text cleaning
* Marks-line detection
* Heading detection
* Question detection
* Question-number removal
* Difficulty classification
* Total-mark extraction
* Final report generation

### `requirements.txt`

Contains the Python packages required by the project:

```text
streamlit
pytesseract
Pillow
```

---

##  Project Workflow

```text
             Exam Paper Image
                    │
                    ▼
              Streamlit App
                    │
                    ▼
                Upload Image
                    │
                    ▼
                Pillow
                    │
                    ▼
             Tesseract OCR
                    │
                    ▼
             Extracted Text
                    │
                    ▼
              Text Cleaning
                    │
                    ▼
            Question Detection
                    │
                    ▼
         Remove Question Numbers
                    │
                    ▼
          Difficulty Classification
             /       |       \
            /        |        \
         Easy      Medium      Hard
                    │
                    ▼
             Marks Detection
                    │
                    ▼
             Generate Report
                    │
                    ▼
             Display Results
```

---

##  Installation

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

Move into the project folder:

```bash
cd AI-Exam-Paper-Analyzer
```

---

### Step 2: Install Python

Make sure Python is installed on your system.

Check the installed version:

```bash
python --version
```

---

### Step 3: Install Required Python Packages

Run:

```bash
pip install -r requirements.txt
```

If `pip` is not recognized, you can use:

```bash
python -m pip install -r requirements.txt
```

---

##  Tesseract OCR Installation

Tesseract OCR must be installed separately because `pytesseract` is a Python interface to the Tesseract OCR program.

The current `ocr.py` is configured for Windows with Tesseract installed at:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

The code contains:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

If Tesseract is installed in another location, update this path in `ocr.py`.

---

## How to Run the Project

Open the project folder in the terminal.

Run:

```bash
streamlit run app.py
```

If the `streamlit` command is not recognized, use:

```bash
python -m streamlit run app.py
```

Streamlit will start the application and provide a local web address.

Open the displayed address in your browser.

---

##  How to Use

### Step 1

Start the Streamlit application:

```bash
streamlit run app.py
```

### Step 2

Upload an exam paper image.

Supported formats:

```text
PNG
JPG
JPEG
```

### Step 3

Click:

```text
 Analyze Exam Paper
```

### Step 4

The application extracts text using OCR.

### Step 5

The extracted text is displayed on the screen.

### Step 6

The analyzer processes the extracted text.

### Step 7

The final report displays:

```text
AI EXAM PAPER ANALYSIS

SUMMARY

Total Questions
Easy Questions
Medium Questions
Hard Questions

TOTAL MARKS

Easy Questions
Medium Questions
Hard Questions

ALL QUESTIONS
```

---

##  How the Analysis Works

### Step 1 — Clean OCR Text

The OCR output is cleaned before analysis.

The application:

* Removes carriage returns.
* Removes unwanted encoded characters.
* Fixes selected OCR mistakes.
* Removes extra spaces.
* Removes multiple blank lines.

---

### Step 2 — Detect Instructions and Marks

The analyzer identifies lines containing patterns such as:

```text
5 x 2
5 x 2 = 10
Each question carries
Part A
Answer any
Section A
```

These lines are ignored during question extraction.

---

### Step 3 — Detect Headings

The analyzer identifies headings such as:

```text
UNIT
PART
SECTION
ANSWER ANY
INSTRUCTIONS
```

These are ignored when extracting questions.

---

### Step 4 — Detect Questions

The analyzer detects question starts using numbered formats:

```text
1. What is DBMS?
2) Define SQL.
```

It also supports Roman numerals:

```text
(i) What is DBMS?
(ii) Define normalization.
```

It can also recognize question words such as:

```text
What is
Define
Explain
Discuss
Describe
List
Identify
How
Why
```

---

### Step 5 — Remove Question Numbers

For example:

```text
1. What is DBMS?
```

becomes:

```text
What is DBMS?
```

Similarly:

```text
(ii) Define normalization.
```

becomes:

```text
Define normalization.
```

---

### Step 6 — Handle Multi-Line Questions

If a question continues across multiple lines, the lines are joined together to form a complete question.

For example:

```text
1. Explain the following
database normalization
techniques with examples.
```

becomes:

```text
Explain the following database normalization techniques with examples.
```

---

### Step 7 — Classify Difficulty

The analyzer checks the question text against predefined keywords.

#### Easy

```text
what is
what are
define
list
write a short note
```

#### Hard

```text
explain
discuss
compare
describe
analyze
evaluate
```

Anything that does not match the Easy or Hard lists is classified as Medium.

---

### Step 8 — Detect Total Marks

The analyzer searches for patterns such as:

```text
5 x 2 = 10
3 x 10 = 30
```

The extracted values are added together.

For example:

```text
5 x 2 = 10
3 x 10 = 30
```

Total:

```text
10 + 30 = 40
```

---

##  Example

Suppose an exam paper contains:

```text
PART A

5 x 2 = 10

1. What is DBMS?
2. Define primary key.
3. Explain normalization.

PART B

3 x 10 = 30

4. Compare SQL and NoSQL.
5. Describe database architecture.
6. Why is normalization important?
```

The application extracts the questions and classifies them according to the predefined rules.

The detected total marks are:

```text
10 + 30 = 40
```

The final report contains separate sections for:

```text
Easy Questions
Medium Questions
Hard Questions
All Questions
```

---

##  Important Note About AI

Although the project is named **AI Exam Paper Analyzer**, the current implementation does not use a trained Machine Learning or Deep Learning model.

The project uses:

```text
OCR
+
Regex
+
Keyword-based rule classification
```

Tesseract performs OCR, while the analyzer uses predefined rules to classify questions.

A future version could use NLP or Machine Learning for more intelligent difficulty classification.

---

##  Limitations

The current version has some limitations:

1. OCR accuracy depends on the quality of the uploaded image.
2. Difficulty classification is keyword-based.
3. Only selected OCR mistakes are corrected.
4. Total-mark detection depends on supported mark formats.
5. The current uploader accepts PNG, JPG, and JPEG images.
6. The project does not currently use a trained ML model.

---

## Future Enhancements

Possible future improvements include:

* PDF exam-paper support.
* Better image preprocessing.
* Automatic noise removal.
* Image rotation and deskewing.
* Improved OCR accuracy.
* Machine-learning-based difficulty classification.
* NLP-based question understanding.
* Automatic subject/topic detection.
* Question-wise mark detection.
* Study recommendations based on question difficulty.
* Question-answer generation.
* Exam paper statistics and visualizations.

---

##  Learning Outcomes

Through this project, the following concepts are demonstrated:

* Python programming
* Functions and modules
* Regular expressions
* Text processing
* OCR
* Image handling
* Streamlit application development
* File uploading
* Rule-based classification
* Basic automation
* Error handling
* Modular project structure

---

##  Project Summary

**Project Name:** AI Exam Paper Analyzer

**Language:** Python

**Interface:** Streamlit

**OCR:** Tesseract OCR

**Image Library:** Pillow

**Text Processing:** Regular Expressions

**Classification:** Rule-based keyword classification

**Input:** Exam paper image

**Output:** Extracted questions, difficulty classification, and detected total marks

---

## 📄 License

This project is created for educational and academic purposes.
