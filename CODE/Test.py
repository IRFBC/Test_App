import tkinter as tk
from tkinter import filedialog
import pandas as pd

questions_df = None
current_question = 0
total_score = 0
questions_list = []
selected_options = []
file_name = ""

def upload_file():
    global file_name
    file_path = filedialog.askopenfilename()
    if file_path:
        file_name = file_path.split('/')[-1]
        load_questions(file_path)

def load_questions(file_path):
    global questions_df, current_question, total_score, questions_list, selected_options
    questions_df = pd.read_excel(file_path)
    questions_list = questions_df.values.tolist()
    current_question = 0
    total_score = 0
    selected_options = []
    show_question()

def show_question():
    global current_question, questions_list, question_text, option_buttons
    if current_question < len(questions_list):
        question_data = questions_list[current_question]
        question = question_data[0]
        options = question_data[1:6]  # Get the first 5 options
        question_text.set(question)
        for i, option in enumerate(options):
            option_buttons[i].config(text=option)
    else:
        show_results()

def select_option(option_index):
    global current_question, total_score, selected_options
    selected_options.append(option_index)
    total_score += option_index
    current_question += 1
    show_question()

def determine_level(score, file_name):
    if file_name == "Book3.xlsx":
        if score <= 10:
            return "Normal"
        elif score <= 16:
            return "Mild Depression"
        elif score <= 20:
            return "Need Consultation"
        elif score <= 30:
            return "Moderate Depression"
        elif score <= 40:
            return "Severe Depression"
        else:
            return "Extreme Depression"
    elif file_name == "Book2.xlsx":
        if 0 <= score <= 7:
            return "Anxious is normal"
        elif 8 <= score <= 15:
            return "Mild Anxious"
        elif 16 <= score <= 25:
            return "Average Anxious"
        elif 26 <= score <= 63:
            return "Severe Anxious"
    else:
        return "Level not defined"

def show_results():
    global total_score, results_text, file_name
    level = determine_level(total_score, file_name)
    results_text.set(f"Total Score: {total_score}\nLevel: {level}")
    save_results()

def save_results():
    global selected_options, file_name
    results_df = pd.DataFrame({'Question': range(1, len(selected_options) + 1), 'Score': selected_options})

    try:
        # Try to open the existing results file
        existing_df = pd.read_excel('results.xlsx', sheet_name=None)
    except FileNotFoundError:
        # If the file does not exist, create an empty dictionary
        existing_df = {}

    # Add the new results to the existing data
    existing_df[file_name.split('.')[0]] = results_df

    # Write all sheets back to the file
    with pd.ExcelWriter('results.xlsx', engine='openpyxl') as writer:
        for sheet_name, df in existing_df.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

def clear_inputs():
    global current_question, total_score, selected_options, question_text, results_text
    current_question = 0
    total_score = 0
    selected_options = []
    question_text.set("")
    results_text.set("")

root = tk.Tk()
root.title("Test")
root.geometry("600x400")
root.config(bg="lightblue")

question_text = tk.StringVar()
question_label = tk.Label(root, textvariable=question_text, wraplength=400, bg="white", fg="black")
question_label.pack(pady=20, padx=20, fill="x", expand=True)

option_buttons = []
for i in range(5):
    btn = tk.Button(root, text="", command=lambda i=i: select_option(i), bg="mintcream", fg="black", activebackground="darkblue", activeforeground="white", borderwidth=2, relief="solid", highlightbackground="darkblue", highlightthickness=2)
    btn.pack(pady=5, padx=20, fill="x", expand=True)
    option_buttons.append(btn)

results_text = tk.StringVar()
results_label = tk.Label(root, textvariable=results_text, bg="white", fg="black")
results_label.pack(pady=20, padx=20, fill="x", expand=True)

upload_btn = tk.Button(root, text="Upload File", command=upload_file, bg="skyblue", fg="black", activebackground="darkblue", activeforeground="white", borderwidth=2, relief="solid", highlightbackground="darkblue", highlightthickness=2)
upload_btn.pack(side="left", padx=20, pady=20)

clear_btn = tk.Button(root, text="Clear Inputs", command=clear_inputs, bg="skyblue", fg="black", activebackground="darkblue", activeforeground="white", borderwidth=2, relief="solid", highlightbackground="darkblue", highlightthickness=2)
clear_btn.pack(side="right", padx=20, pady=20)

root.mainloop()
