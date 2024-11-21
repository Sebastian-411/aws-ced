# Recommendation Analysis Application with Chatbot

This project is a web application that allows you to interact with a chatbot to receive personalized recommendations. Follow the steps below to run it.

## Access the Application

You can access the application directly at the following link:

[http://ec2-3-145-202-108.us-east-2.compute.amazonaws.com:5173/](http://ec2-3-145-202-108.us-east-2.compute.amazonaws.com:5173/)

1. **Login**: If you already have an account, simply log in. If you don't have an account, register to create one.
2. **Chatbot Interaction**: After logging in, you will be redirected to a chat with the chatbot. The chatbot will ask you questions, and based on your answers, it will provide you with an analysis and personalized recommendations.
3. **Random Questions**: The system will randomly select 10 questions to give you a unique experience.

## Run the Application Locally

If you want to run the application locally, follow these steps:

### Prerequisites

- Docker installed on your machine.

### Steps to Run:

1. Navigate to the `frontend` folder in your project.
2. Look for the `Dockerfile` in that folder and run the following command:

   ```bash
   docker build -t frontend .
   docker run -p 5173:5173 frontend
   ```

3. Next, navigate to the `backend/chatbot` folder and look for the `Dockerfile`. Run the following commands to build and run the backend container:

   ```bash
   docker build -t backend-chatbot .
   docker run -p 5000:5000 backend-chatbot
   ```

4. Once both containers are running, open your browser and go to:

   ```
   http://localhost:5173
   ```

That's it! You can now interact with the application locally.
