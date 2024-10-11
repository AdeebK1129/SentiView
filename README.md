# **SentiView**

## **Overview**

SentiView is a real-time product/customer review analytics platform designed to collect, analyze, and visualize customer feedback. The platform allows users to monitor customer reviews in real time, perform sentiment analysis, and trigger alerts for urgent feedback. It is built as a SaaS platform and is designed to scale, offering features such as user authentication with OAuth, 2FA, and customizable surveys.

## **Features**
- **Real-time Feedback Monitoring**: Gather customer feedback from various sources and analyze it in real time.
- **Sentiment Analysis**: Uses NLP algorithms to classify customer feedback as positive, neutral, or negative.
- **Alerts for Urgent Trends**: Sends alerts when urgent or high-priority feedback is detected.
- **Custom Surveys**: Allows companies to gather additional information about their users with dynamic survey forms.
- **User Authentication**: Secure sign-up process with options for OAuth (e.g., Google), and 2FA.

## **Project Structure**

### **Frontend (React + TypeScript)**
- **TypeScript** is used for type safety and scalability.
- **React Query** is used for handling server-side data and HTTP requests.
- **React** is used for the frontend user interface.
- **Axios** is used for handling API requests from the backend.

### **Backend (Django + PostgreSQL)**
- **Django** is used as the backend framework.
- **Django REST Framework** handles API endpoints.
- **PostgreSQL** is used for data persistence, ideal for relational data and scalable systems.
- **NLP Pipeline** is set up to process and analyze customer feedback.
- **Channels** are used for handling real-time functionality.

## **Table of Contents**

- [Getting Started](#getting-started)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [File Structure](#file-structure)
- [Contributing](#contributing)

## **Getting Started**

### **Prerequisites**
Before running this project, ensure you have the following installed on your system:
- **Node.js** (>=14.x)
- **Python** (>=3.8)
- **PostgreSQL** (>=13.x)
- **npm** or **yarn**

### **Tech Stack**
- **Frontend**: React, TypeScript, Axios, React Query
- **Backend**: Django, Django REST Framework, Channels, PostgreSQL
- **Data Pipeline**: NLP (Natural Language Processing), Sentiment Analysis
- **Database**: PostgreSQL

## **Installation**

### **Backend Setup**
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/sentiview.git
    cd sentiview/backend
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install --upgrade pip-tools
    pip-sync requirements_env/main.txt requirements_env/dev.txt
    ```

4. Create a `secrets.json` file inside the `backend` directory with the following structure:
    ```json
    {
      "SECRET_KEY": "your-secret-key",
      "DATABASE_NAME": "your-database-name",
      "DATABASE_USER": "your-database-user",
      "DATABASE_PASSWORD": "your-database-password",
      "DATABASE_HOST": "localhost",
      "DATABASE_PORT": "5432"
    }
    ```

    Replace the placeholder values with your own database information.

5. Run migrations and start the Django development server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

### **Frontend Setup**
1. Navigate to the `frontend` folder:
    ```bash
    cd ../frontend
    ```

2. Install the frontend dependencies:
    ```bash
    npm install
    ```

3. Run the development server:
    ```bash
    npm start
    ```

### **Usage**
After setting up both the frontend and backend, you can access the platform at:
- **Frontend**: `http://localhost:3000`
- **Backend**: `http://localhost:8000`

To test the connection between the frontend and backend, the homepage should display the "Hello, World!" message fetched from the Django backend API.

## **API Endpoints**

### **GET /api/hello/**
- Returns a simple JSON response:
    ```json
    {
      "message": "Hello, World!"
    }
    ```

### **POST /api/survey-response/**
- Submits user survey responses.

### **GET /api/customer-feedback/**
- Fetches customer feedback for analysis.

### **POST /api/feedback-analysis/**
- Submits feedback for real-time NLP analysis.

## **File Structure**
The project is organized into two main directories: `frontend` and `backend`.

### **Backend**
backend/ |-- api/ | |-- views.py # API views for handling requests | |-- urls.py # URL routing for the API |-- manage.py # Django project management script |-- settings.py # Project settings and configuration |-- requirements_env/ | |-- main.txt # Production dependencies | |-- dev.txt # Development dependencies


### **Frontend**
frontend/ |-- src/ | |-- components/ # React components | |-- queries.ts # Handles API requests using React Query and Axios | |-- App.tsx # Main React app |-- package.json # Frontend dependencies |-- tsconfig.json # TypeScript configuration


## **Contributing**

We welcome contributions! Please follow these guidelines to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes with clear messages adhering to the [Commit Message Guide](https://google.github.io/styleguide/gitguide.html).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.
