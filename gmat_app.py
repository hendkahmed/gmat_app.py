import streamlit as st
import time

# ------------------ Test Data ------------------
test_data = {
    "quantitative": {
        "title": "Quantitative Section",
        "description": "This section contains 31 questions to be completed in 62 minutes.",
        "note": "You'll have access to an on-screen calculator for this section only.",
        "questions": [
            {
                "id": "quant-q1",
                "text": "1. If x and y are positive integers such that x + y = 8, what is the maximum possible value of xy?",
                "options": ["A) 12", "B) 15", "C) 16", "D) 18", "E) 20"],
                "correct_answer": "C",
                "explanation": "The maximum product occurs when x and y are as close as possible. For x + y = 8, the closest pairs are (3,5) and (4,4). The product for (3,5) is 15, while for (4,4) it's 16."
            },
            {
                "id": "quant-q2",
                "text": "2. A train travels 300 miles in 5 hours. If it travels at a constant speed, how many miles will it travel in 7 hours?",
                "options": ["A) 350", "B) 400", "C) 420", "D) 450", "E) 500"],
                "correct_answer": "C",
                "explanation": "Speed = 300 / 5 = 60 mph. Distance = 60 * 7 = 420 miles."
            },
            {
                "id": "quant-q3",
                "text": "3. If 3x - 7 = 17, what is the value of x?",
                "options": ["A) 6", "B) 8", "C) 10", "D) 12", "E) 14"],
                "correct_answer": "B",
                "explanation": "3x - 7 = 17 → 3x = 24 → x = 8 (Option B)."
            }
        ]
    },
    "verbal": {
        "title": "Verbal Section",
        "description": "This section contains 31 questions to be completed in 65 minutes.",
        "note": "The section includes Reading Comprehension, Critical Reasoning, and Sentence Correction questions.",
        "questions": [
            {
                "id": "verbal-q1",
                "text": "1. The company's profits have increased significantly over the past year, ______ due to its successful marketing campaign and improved product quality.",
                "options": ["A) largely", "B) large", "C) largest", "D) the large", "E) the largely"],
                "correct_answer": "A",
                "explanation": "'Largely' is an adverb modifying 'due'. Other choices are incorrect forms."
            },
            {
                "id": "verbal-q2",
                "text": "2. Which of the following best completes the passage?\n\nMany economists argue that free trade benefits all participating nations. However, critics contend that ______.",
                "options": ["A) free trade leads to greater economic growth", "B) the benefits are not equally distributed", "C) tariffs should be eliminated completely", "D) international cooperation is essential", "E) protectionist policies are outdated"],
                "correct_answer": "B",
                "explanation": "Only B presents a proper contrast to the opening statement."
            }
        ]
    },
    "ir": {
        "title": "Integrated Reasoning Section",
        "description": "This section contains 12 questions to be completed in 30 minutes.",
        "note": "You'll encounter multi-source reasoning, graphics interpretation, and other question types.",
        "questions": [
            {
                "id": "ir-q1",
                "text": "1. Based on the information in the table, which product showed the highest percentage increase in sales from Q1 to Q2?",
                "options": ["A) Product A", "B) Product B", "C) Product C", "D) Product D", "E) Product E"],
                "correct_answer": "C",
                "explanation": "Compare % increase for all and select the highest. (Product C)"
            },
            {
                "id": "ir-q2",
                "text": "2. The graph shows the company's revenue and expenses over five years. In which year was the profit margin the highest?",
                "options": ["A) 2018", "B) 2019", "C) 2020", "D) 2021", "E) 2022"],
                "correct_answer": "B",
                "explanation": "Profit margin = (Revenue - Expenses) / Revenue. Calculate and compare."
            }
        ]
    }
}

# ------------------ Session Setup ------------------
if "section" not in st.session_state:
    st.session_state.section = "quantitative"
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

# ------------------ Sidebar Navigation ------------------
st.sidebar.title("GMAT Sections")
selected_section = st.sidebar.radio("Choose a section:", list(test_data.keys()))

if selected_section != st.session_state.section:
    st.session_state.section = selected_section
    st.session_state.current_q = 0
    st.session_state.answers = {}

# ------------------ Main Quiz ------------------
section = test_data[st.session_state.section]
questions = section["questions"]

st.title(section["title"])
st.write(section["description"])
st.info(section["note"])

current_q = st.session_state.current_q
if current_q >= len(questions):
    st.success("🎉 You've completed this section!")

    score = sum(1 for a in st.session_state.answers.values() if a["correct"])
    total = len(questions)
    percent = int((score / total) * 100)

    st.info(f"Your score: {score}/{total} ({percent}%)")
    if percent >= 80:
        st.success("Excellent performance! You're well prepared for the GMAT.")
    elif percent >= 60:
        st.warning("Good job! With some more practice, you'll be ready.")
    else:
        st.error("Keep practicing! Review the questions you missed.")

    if st.button("Restart Section"):
        st.session_state.current_q = 0
        st.session_state.answers = {}
else:
    question = questions[current_q]
    st.subheader(question["text"])
    selected = st.radio("Choose one:", question["options"], key=question["id"])

    if st.button("Submit Answer"):
        correct_letter = question["correct_answer"]
        user_letter = selected.split(")")[0]

        is_correct = user_letter == correct_letter
        if is_correct:
            st.success(f"✅ Correct! {question['explanation']}")
        else:
            correct_option = [opt for opt in question["options"] if opt.startswith(correct_letter)][0]
            st.error(f"❌ Incorrect. Correct answer: {correct_option}\n\n{question['explanation']}")

        st.session_state.answers[question["id"]] = {
            "selected": user_letter,
            "correct": is_correct
        }
        st.session_state.current_q += 1

    progress = int(((current_q + 1) / len(questions)) * 100)
    st.progress(progress)
