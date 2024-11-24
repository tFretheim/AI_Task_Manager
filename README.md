# AI_Task_Manager

AI Task Manager
AI Task Manager is a Flask-based web application that leverages artificial intelligence to predict and manage task priorities. The application allows users to add tasks with titles and descriptions, and the AI-powered model automatically determines the priority of each task based on the content of the task description. The tasks are stored in an SQLite database and can be retrieved in order of priority.

Features
Task Management: Users can add new tasks, view all tasks, and see them sorted by priority.
AI-Powered Priority Prediction: The application uses a machine learning model to automatically predict the priority of tasks based on their titles and descriptions.
SQLite Database: All tasks are stored in an SQLite database for persistence.

Technologies Used
Flask: A micro web framework for Python that is used to build the web application.
SQLite: A lightweight database engine used to store tasks.
Scikit-learn: A machine learning library used to train a text classification model that predicts task priority based on the title and description.
HTML/CSS/JavaScript: Basic frontend technologies used to build the user interface.

Project Setup
Prerequisites
Python 3.8 or higher
Flask
Scikit-learn
SQLite (comes pre-installed with Python)

Steps to Set Up
Clone the repository to your local machine:

bash:
git clone https://github.com/tFretheim/ai-task-manager.git
cd ai-task-manager
Set up a virtual environment (optional but recommended):

bash:
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
Install the required dependencies:

bash
pip install -r requirements.txt
Initialize the SQLite database:

bash:
python app.py
This will create the database.db file and set up the necessary table for storing tasks.

Run the application:

bash:
python app.py
The application will be accessible at http://127.0.0.1:5000/ in your web browser.

Functionality
Home Page (/): The main page where users can input new tasks (title and description). When a user submits a new task, the AI model will predict its priority based on the text content, and the task will be saved to the database with the predicted priority.

Add Task (/add_task): The backend endpoint where new tasks are added via a POST request. The request body should contain the task title and description. The priority is predicted by the machine learning model, and the task is stored in the database.

Get Tasks (/tasks): This endpoint fetches all tasks from the database, sorted by priority (high to low). It returns a JSON array containing the tasks' titles, descriptions, and priorities.

How the AI Works
The AI component of the project is a text classification model that predicts the priority of a task based on its title and description. The model is trained using a set of example tasks with known priorities, and it uses Naive Bayes classification to predict the priority level for new tasks.

Training Data: The model is trained on tasks that have both a description and a manually assigned priority. Each task's description is processed using CountVectorizer to convert the text into numerical features, which are then used to train the model.
Prediction: When a new task is added, the model predicts its priority by analyzing the title and description. The priority is then stored in the database alongside the task.
Example Workflow
A user visits the homepage and inputs a new task with a title and description.
The task data is sent to the backend, where the model predicts the task's priority based on the description.
The task, along with the predicted priority, is stored in the SQLite database.
Users can view all tasks sorted by priority.
Contributing
Contributions are welcome! Feel free to fork the repository, create a pull request, or open an issue to discuss improvements.

Tips for Improvement
User Authentication: You can add user authentication so that multiple users can manage their own tasks.
Task Editing: Allow users to edit or delete tasks.
Advanced ML Models: Train more complex machine learning models (e.g., using deep learning techniques) to improve task priority prediction.
User Interface Improvements: Enhance the user interface using frontend frameworks like Bootstrap for better aesthetics and responsiveness.
