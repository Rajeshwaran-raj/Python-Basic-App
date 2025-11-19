# Python-Basic-App

A simple Python application that connects to a MySQL database and performs basic operations.

## 📌 Database Setup

Run the following SQL commands to create the database and insert sample data:

```
CREATE DATABASE exampledb;

USE exampledb;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL
);

INSERT INTO users (name, age) VALUES 
('Rajeshwaran', 24),
('Sanjay', 28),
('Priya', 22),
('Arun', 30),
('Meena', 26);
```

## 🚀 How to Run the Application

1. Install dependencies

   ```
   pip install -r requirements.txt
   ```

2. Set up your environment variables (DB credentials)

3. Start the application

   ```
   python app.py
   ```

## 📂 Project Name

**Python-Basic-App**

This project demonstrates basic Python–MySQL integration using Flask/SQLAlchemy.
