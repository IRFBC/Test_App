# Test APP

## Overview

This project aims to develop a dataset for designing an AI model focused on identifying patterns in depression, anxiety, and other related mental health conditions. The model, based on NLP (Natural Language Processing) structure, will serve as an assistant to psychiatrists. It will provide various services, including data analysis, preclinical diagnosis, and treatment prediction, as well as monitoring and control of treatment.

## Features

- **Upload and Load Questionnaires**: Easily upload Excel files containing mental health questionnaires.
- **Interactive Question Interface**: Navigate through questions and select answers with a user-friendly GUI.
- **Score Calculation and Interpretation**: Automatically calculate the total score and determine the level of depression or anxiety based on predefined criteria.
- **Save Results**: Save the questionnaire results to an Excel file for future reference and analysis.
- **Clear Inputs**: Reset the interface for a new questionnaire session.

## Requirements

- Python 3.x
- `tkinter` for GUI
- `pandas` for data handling
- `openpyxl` for Excel file operations

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/IRFBC/Test_App.git
    cd Test_App
    ```

2. **Install the required packages**:
    ```bash
    pip install pandas openpyxl
    ```

## Usage

1. **Run the application**:
    ```bash
    python Test.py
    ```

2. **Upload the questionnaire file**: Click on the "Upload File" button and select an Excel file with the questionnaire.

3. **Answer the questions**: Navigate through the questions and select the appropriate options.

4. **View results**: After completing the questionnaire, view the total score and the interpreted level of depression or anxiety.

5. **Save results**: The results will be saved to `results.xlsx` for future analysis.

6. **Clear inputs**: Click on the "Clear Inputs" button to reset the interface for a new session.

## Example Files

- [Book2.xlsx](https://github.com/IRFBC/Test_App/blob/main/FORMS/Book2.xlsx): Contains questions related to anxiety.
- [Book3.xlsx](https://github.com/IRFBC/Test_App/blob/main/FORMS/Book3.xlsx): Contains questions related to depression.

## Contributing

1. **Fork the repository**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature-branch
    ```
3. **Make your changes** and commit them:
    ```bash
    git commit -m "Description of changes"
    ```
4. **Push to the branch**:
    ```bash
    git push origin feature-branch
    ```
5. **Create a pull request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



## Future Work

- **Enhancing NLP Capabilities**: Improve the NLP model to provide more accurate preclinical diagnoses and treatment recommendations.
- **Integration with Electronic Health Records (EHR)**: Seamless integration with EHR systems for better data management and analysis.
- **Real-time Monitoring**: Implement real-time monitoring and feedback for patients undergoing treatment.

By developing this project, we aim to leverage AI and NLP technologies to assist psychiatrists in providing better mental health care, ultimately improving patient outcomes.

## image of page : 
![Screenshot 2024-07-14 223837](https://github.com/user-attachments/assets/9daf2427-3bb9-4228-95ca-1edcc1aedde1)

## show result in page :

![Screenshot 2024-07-14 223002](https://github.com/user-attachments/assets/35587049-7ea3-43e4-a04d-3af08453173e)


## image of out put xlsx

![Screenshot 2024-07-14 223536](https://github.com/user-attachments/assets/5206d126-0402-47cd-9636-0bc2e0a7ac6b)

