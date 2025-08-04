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
            },
            {
                "id": "quant-q4",
                "text": "4. What is the area of a circle with circumference 10π?",
                "options": ["A) 5π", "B) 10π", "C) 20π", "D) 25π", "E) 100π"],
                "correct_answer": "D",
                "explanation": "Circumference = 2πr = 10π → r = 5. Area = πr² = 25π."
            },
            {
                "id": "quant-q5",
                "text": "5. If 2^x = 32, what is the value of x?",
                "options": ["A) 2", "B) 3", "C) 4", "D) 5", "E) 6"],
                "correct_answer": "D",
                "explanation": "32 = 2^5, so x = 5."
            },
            {
                "id": "quant-q6",
                "text": "6. The average of five numbers is 20. If one number is removed, the average becomes 18. What was the number removed?",
                "options": ["A) 22", "B) 24", "C) 26", "D) 28", "E) 30"],
                "correct_answer": "D",
                "explanation": "Total of 5 numbers = 100. Total of 4 numbers = 72. Removed number = 100 - 72 = 28."
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
            },
            {
                "id": "verbal-q3",
                "text": "3. Identify the grammatically correct sentence:",
                "options": ["A) Neither the manager nor the employees was aware of the policy change.", "B) Each of the students have completed their assignments.", "C) The data suggests that the new treatment is effective.", "D) The committee are divided in their opinions.", "E) A number of people was absent yesterday."],
                "correct_answer": "C",
                "explanation": "Option C is correct. 'Data' can be singular, and the verb agrees. Other options have subject-verb agreement errors."
            },
            {
                "id": "verbal-q4",
                "text": "4. The author's argument would be most weakened if which of the following were true?",
                "options": ["A) The sample size was larger than initially reported", "B) The control group showed similar results", "C) The experiment was conducted by independent researchers", "D) The results were consistent across different demographics", "E) The measurement tools were found to be unreliable"],
                "correct_answer": "E",
                "explanation": "If measurement tools were unreliable, the entire study's validity would be compromised."
            },
            {
                "id": "verbal-q5",
                "text": "5. Choose the word most opposite in meaning to 'EPHEMERAL':",
                "options": ["A) Temporary", "B) Fleeting", "C) Permanent", "D) Transient", "E) Momentary"],
                "correct_answer": "C",
                "explanation": "Ephemeral means lasting for a short time, so 'permanent' is its opposite."
            },
            {
                "id": "verbal-q6",
                "text": "6. The passage suggests that the primary cause of the economic downturn was:",
                "options": ["A) Decreased consumer spending", "B) Government policy changes", "C) Fluctuations in the stock market", "D) Overregulation of industries", "E) A combination of external factors"],
                "correct_answer": "A",
                "explanation": "The passage emphasizes reduced consumer confidence and spending as the main factor."
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
            },
            {
                "id": "ir-q3",
                "text": "3. If the trend shown in the chart continues, what will be the approximate value in 2023?",
                "options": ["A) 120", "B) 135", "C) 150", "D) 165", "E) 180"],
                "correct_answer": "D",
                "explanation": "Extend the trend line to estimate the 2023 value."
            },
            {
                "id": "ir-q4",
                "text": "4. Based on the two sources provided, which conclusion is best supported?",
                "options": ["A) Sales are declining in all regions", "B) The new marketing strategy is effective", "C) Customer satisfaction has decreased", "D) Production costs are rising", "E) Employee turnover is increasing"],
                "correct_answer": "B",
                "explanation": "Both sources provide evidence supporting the effectiveness of the new strategy."
            },
            {
                "id": "ir-q5",
                "text": "5. Which region showed the greatest variance between projected and actual sales?",
                "options": ["A) North", "B) South", "C) East", "D) West", "E) Central"],
                "correct_answer": "A",
                "explanation": "Calculate the differences for each region and compare."
            },
            {
                "id": "ir-q6",
                "text": "6. Based on the table, if the growth rate remains constant, what will be the value in Year 5?",
                "options": ["A) 1,200", "B) 1,440", "C) 1,728", "D) 2,074", "E) 2,488"],
                "correct_answer": "D",
                "explanation": "Calculate the growth rate and apply it to project Year 5's value."
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
    
    # Use a form to prevent the page from reloading when moving to next question
    with st.form(key='question_form'):
        selected = st.radio("Choose one:", question["options"], key=question["id"])
        
        col1, col2 = st.columns(2)
        with col1:
            submit_button = st.form_submit_button("Submit Answer")
        with col2:
            next_button = st.form_submit_button("Next Question")
        
        if submit_button:
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
        
        if next_button:
            st.session_state.current_q += 1
            st.experimental_rerun()

    progress = int(((current_q + 1) / len(questions)) * 100
    st.progress(progress)
