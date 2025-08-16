
---

# Complexity_Quiz

A web-based Python quiz application that dynamically generates questions to test your understanding of code complexity and iteration counting.

## 📖 Description

**Complexity_Quiz** is a web application built with Flask that leverages the power of Google's Generative AI to create an interactive learning experience. Users can select a difficulty level (from 1 to 3), and the application will generate a Python code snippet. The challenge is to correctly determine the total number of iterations the code will perform.

This project is an excellent demonstration of how to integrate a powerful AI model into a web framework to create dynamic and educational content.

## ✨ Features

-   **Dynamic Quiz Generation**: Questions are not hard-coded; they are generated on-the-fly by the Google Generative AI API.
-   **Variable Complexity Levels**: Users can choose from three different levels of code complexity to match their skill level.
-   **Interactive Interface**: A clean and simple user interface for selecting complexity, viewing code, and submitting answers.
-   **Instant Feedback**: The application immediately informs the user if their answer was correct and provides the right solution.
-   **Flask Framework**: Built on a lightweight and powerful Python web framework.

## 🛠️ Technologies Used

-   **Backend**: Python, Flask
-   **Frontend**: HTML, CSS
-   **AI**: Google Generative AI (Gemini)

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.7+
-   A Google API key with the Generative AI (Gemini) API enabled. You can get one from the [Google AI Studio](https://aistudio.google.com/app/apikey).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/azario0/Complexity_Quiz.git
    cd Complexity_Quiz
    ```

2.  **Create and activate a virtual environment:**
    -   **On macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    -   **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file. See the section below.)*

4.  **Set up your environment variables:**
    Create a `.env` file in the root of your project and add your Google API key:
    ```
    GEMINI_API_KEY=YOUR_API_KEY_HERE
    ```

    Then, modify `app.py` to load this key securely instead of hardcoding it. Replace:
    ```python
    genai.configure(api_key="AIzaSyDviegMUvTr2cYL4KFSLIRnQPyqcPyD13w")
    ```
    with:
    ```python
    from dotenv import load_dotenv
    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    ```
    *(Don't forget to add `python-dotenv` to your `requirements.txt` file and install it.)*


### Running the Application

Once you have completed the setup, you can run the application with the following command:

```bash
flask run
```

Open your web browser and navigate to `http://127.0.0.1:5000` to start using the quiz app.

## usage How to Use

1.  **Home Page**: You will be prompted to select a complexity level from 1 to 3.
2.  **Start Quiz**: Enter your desired level and click "Start Quiz".
3.  **Quiz Page**: The application will display a Python code snippet. Analyze the code to determine how many iterations it will execute.
4.  **Submit Answer**: Click on one of the three multiple-choice buttons to submit your answer.
5.  **Get Feedback**: A message will appear at the top, telling you if you were correct.
6.  **Try Again**: You can try another question at the same complexity or click "Change Complexity" to return to the home page.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, please feel free to fork the repository and submit a pull request.

---