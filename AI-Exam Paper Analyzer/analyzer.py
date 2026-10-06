import re


# ==========================================
# 1. CLEAN OCR TEXT
# ==========================================

def clean_text(text):

    text = text.replace("\r", "\n")
    text = text.replace("&#xD;", "")

    # Fix common OCR mistakes
    text = text.replace("Kxplain", "Explain")
    text = text.replace("Kxplain", "Explain")
    text = text.replace("Wnite", "Write")

    # Remove extra spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Remove multiple blank lines
    text = re.sub(r"\n+", "\n", text)

    return text.strip()


# ==========================================
# 2. CHECK MARKS / INSTRUCTION LINE
# ==========================================

def is_marks_line(line):

    patterns = [
        r"\d+\s*[x×]\s*\d+\s*marks?",
        r"\d+\s*[x×]\s*\d+",
        r"each question carries",
        r"marks\s*=",
        r"part\s+[a-d]",
        r"answer any",
        r"section\s+[a-d]"
    ]

    for pattern in patterns:

        if re.search(pattern, line, re.IGNORECASE):
            return True

    return False


# ==========================================
# 3. CHECK HEADINGS
# ==========================================

def is_heading(line):

    headings = [
        "unit",
        "part",
        "section",
        "answer any",
        "instructions"
    ]

    line_lower = line.lower().strip()

    for word in headings:

        if line_lower.startswith(word):
            return True

    return False


# ==========================================
# 4. CHECK QUESTION START
# ==========================================

def is_question_start(line):

    line_lower = line.lower().strip()

    # Example:
    # 1. What is DBMS?
    # 2) What is SQL?

    if re.match(r"^\d+[\.\)]\s*", line):
        return True

    # Example:
    # (i) What is DBMS?
    # (ii) Define normalization.

    if re.match(
        r"^\(?[ivxlcdm]+\)?[\.\)]?\s+",
        line,
        re.IGNORECASE
    ):
        return True

    # Question words

    question_words = [
        "what is",
        "what are",
        "what do",
        "what does",
        "define",
        "describe",
        "discuss",
        "explain",
        "write",
        "list",
        "identify",
        "how",
        "why"
    ]

    for word in question_words:

        if line_lower.startswith(word):
            return True

    return False


# ==========================================
# 5. REMOVE QUESTION NUMBER
# ==========================================

def remove_question_number(line):

    # Remove 1. / 2) / 10.
    line = re.sub(
        r"^\d+[\.\)]\s*",
        "",
        line
    )

    # Remove (i) / (ii) / (iii)
    line = re.sub(
        r"^\(?[ivxlcdm]+\)?[\.\)]?\s*",
        "",
        line,
        flags=re.IGNORECASE
    )

    return line.strip()


# ==========================================
# 6. EXTRACT QUESTIONS
# ==========================================

def extract_questions(text):

    text = clean_text(text)

    lines = text.split("\n")

    questions = []

    current_question = ""

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Ignore marks
        if is_marks_line(line):
            continue

        # Ignore headings
        if is_heading(line):
            continue

        # Ignore page number
        if re.match(r"^[A-Z]-\d+", line):
            continue

        # New question
        if is_question_start(line):

            # Save previous question
            if current_question:

                questions.append(
                    current_question.strip()
                )

            # Start new question
            current_question = remove_question_number(line)

        else:

            # Continue previous question
            if current_question:

                current_question += " " + line

    # Save last question
    if current_question:

        questions.append(
            current_question.strip()
        )

    return questions


# ==========================================
# 7. DIFFICULTY CLASSIFICATION
# ==========================================

def calculate_difficulty(questions):

    easy_questions = []
    medium_questions = []
    hard_questions = []

    easy_words = [
        "what is",
        "what are",
        "define",
        "list",
        "write a short note"
    ]

    hard_words = [
        "explain",
        "discuss",
        "compare",
        "describe",
        "analyze",
        "evaluate"
    ]

    for question in questions:

        q = question.lower().strip()

        # Hard
        if any(word in q for word in hard_words):

            hard_questions.append(question)

        # Easy
        elif any(word in q for word in easy_words):

            easy_questions.append(question)

        # Medium
        else:

            medium_questions.append(question)

    return (
        easy_questions,
        medium_questions,
        hard_questions
    )


# ==========================================
# 8. FIND TOTAL MARKS
# ==========================================

def extract_total_marks(text):

    marks = []

    # Example:
    # 5 x 2 = 10
    # 3 x 10 = 30

    pattern = r"\d+\s*[x×]\s*\d+\s*=\s*(\d+)"

    matches = re.findall(
        pattern,
        text,
        re.IGNORECASE
    )

    for match in matches:

        marks.append(int(match))

    if marks:

        return sum(marks)

    return 0


# ==========================================
# 9. MAIN ANALYSIS FUNCTION
# ==========================================

def analyze_questions(text):

    # Extract questions
    questions = extract_questions(text)

    # Remove duplicates
    questions = list(dict.fromkeys(questions))

    # Total
    total_questions = len(questions)

    # Difficulty
    (
        easy_questions,
        medium_questions,
        hard_questions
    ) = calculate_difficulty(questions)

    # Marks
    total_marks = extract_total_marks(text)

    # ======================================
    # CREATE OUTPUT
    # ======================================

    result = ""

    result += "## 🤖 AI EXAM PAPER ANALYSIS\n\n"

    # SUMMARY
    result += "## 📊 SUMMARY\n\n"

    result += (
        f"**Total Questions:** "
        f"{total_questions}\n\n"
    )

    result += (
        f"**Easy Questions:** "
        f"{len(easy_questions)}\n\n"
    )

    result += (
        f"**Medium Questions:** "
        f"{len(medium_questions)}\n\n"
    )

    result += (
        f"**Hard Questions:** "
        f"{len(hard_questions)}\n\n"
    )

    # TOTAL MARKS
    result += "## 💯 TOTAL MARKS\n\n"

    if total_marks > 0:

        result += (
            f"**Total Marks:** "
            f"{total_marks}\n\n"
        )

    else:

        result += (
            "**Total Marks:** "
            "Not detected\n\n"
        )

    # EASY
    result += "## 🟢 EASY QUESTIONS\n\n"

    if easy_questions:

        for i, question in enumerate(
            easy_questions,
            1
        ):

            result += (
                f"**{i}.** "
                f"{question}\n\n"
            )

    else:

        result += "No easy questions found.\n\n"

    # MEDIUM
    result += "## 🟡 MEDIUM QUESTIONS\n\n"

    if medium_questions:

        for i, question in enumerate(
            medium_questions,
            1
        ):

            result += (
                f"**{i}.** "
                f"{question}\n\n"
            )

    else:

        result += "No medium questions found.\n\n"

    # HARD
    result += "## 🔴 HARD QUESTIONS\n\n"

    if hard_questions:

        for i, question in enumerate(
            hard_questions,
            1
        ):

            result += (
                f"**{i}.** "
                f"{question}\n\n"
            )

    else:

        result += "No hard questions found.\n\n"

    # ALL QUESTIONS
    result += "## 📝 ALL QUESTIONS\n\n"

    if questions:

        for i, question in enumerate(
            questions,
            1
        ):

            result += (
                f"**{i}.** "
                f"{question}\n\n"
            )

    else:

        result += "No questions detected."

    return result
    