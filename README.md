# TaskMaster API

TaskMaster API is a **backend API** built with **Django** and **Django REST Framework** that allows users to manage their tasks efficiently. Users can create, update, delete, and mark tasks as complete or incomplete while maintaining secure access through authentication.

## Features

- **Task Management (CRUD):** Create, read, update, delete tasks.
- **Task Attributes:** Title, Description, Due Date, Priority (Low, Medium, High), Status (Pending, Completed).
- **User Management:** Register, login, and manage users.
- **Task Ownership:** Each user can only access their own tasks.
- **Mark Complete/Incomplete:** Tasks can be marked complete with timestamps.
- **Filters and Sorting:** Filter tasks by status, priority, and due date; sort by due date or priority.
- **Error Handling:** Proper responses for invalid inputs or unauthorized actions.

## Technologies Used

- **Django** – Backend framework  
- **Django REST Framework (DRF)** – API development  
- **SQLite / PostgreSQL** – Database  
- **JWT (Optional)** – Token-based authentication  

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abel19/taskmaster-api.git
