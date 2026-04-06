# Argument Capital Project (With MongoDB Integration) 🚀

[![Project Status](https://img.shields.io/badge/status-active-success)](https://github.com/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A modern desktop ATM simulation application built with Python, featuring user authentication, transaction management, administrative controls for banking operations, and integrated live chat support using MongoDB.

---

## 🌟 Project Overview

Argument Capital ATM Machine is a comprehensive desktop application that simulates a full-featured ATM system with real-time chat support. It provides users with secure access to banking operations including deposits, withdrawals, balance inquiries, and transaction history, while offering administrators powerful tools to manage users and monitor system activity. The application includes a live chat support system powered by MongoDB for seamless customer assistance.

This project addresses the need for a reliable, user-friendly ATM interface that can be easily deployed on desktop environments, combining intuitive GUI design with robust data persistence (JSON for accounts, MongoDB for chat) and modular architecture for maintainable banking software.

---

## ✨ Key Features

- **Secure User Authentication**: PIN-based login with account blocking after failed attempts.
- **ATM Operations**: Deposit, withdrawal, transfer, and balance checking with real-time updates.
- **Transaction History**: Detailed logs of all financial transactions with timestamps.
- **Admin Panel**: Comprehensive user management, account oversight, and system controls.
- **Live Chat Support**: Real-time customer support chat system using MongoDB for persistent messaging.
- **Modern GUI**: Sleek interface using `customtkinter` with dark mode support.
- **Dual Data Persistence**: JSON-based storage for accounts and transactions, MongoDB for chat sessions.
- **Modular Architecture**: Separated UI, business logic, storage, and chat layers for easy extension.
- **Cross-Platform Compatibility**: Native support for Windows and macOS with platform-specific UI optimizations.

---

## 📁 File Structure

```text
ArgumentCapitalProject/
├── `main.py`                  # Main application entry point for Windows
├── `main_mac.py`              # Main application entry point for macOS
├── `models.py`                # Domain models and business logic definitions
├── `storage.py`               # Local JSON storage layer and persistence utilities
├── `support_manager.py`       # MongoDB-based chat support management system
├── `data.json`                # JSON data store for application state (accounts, transactions)
├── `README.md`                # Project documentation
├── `requirements.txt`         # Python dependencies for the project
├── `.env`                     # Environment variables (MongoDB URI, etc.)
├── `ui_windows/`              # UI modules and components
│   ├── `ui_admin_login.py`     # Admin login screen implementation
│   ├── `ui_admin_panel.py`     # Admin dashboard panel with chat support
│   ├── `ui_admin_user_table.py`# User management interface
│   ├── `ui_dashboard.py`       # Main user dashboard with chat integration
│   ├── `test_final_ui.py`      # Windows UI implementation
│   ├── `test_ui_mac.py`        # macOS UI implementation
│   └── `support_manager.py`    # Chat support manager (MongoDB integration)
└── `__init__.py`              # Package initialization marker
```

---

## 🛠 Installation

### Prerequisites
- Python 3.10 or higher
- MongoDB Atlas account or local MongoDB instance
- MAKE SURE TO USE REGULAR (100%) DISPLAY SCALING! --IMPORTANT-- (הוראות אלו נכתבו בדם)
- Git

### Setup Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ArgumentCapitalMongoDBchat
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MongoDB:**
   - Create a MongoDB Atlas cluster or set up a local MongoDB instance
   - Create a database named `ArgumentCapitalChatDB`
   - Create a collection named `support_chats`
   - Obtain your MongoDB connection string

4. **Configure environment variables:**
   - Create a `.env` file in the root directory
   - Add your MongoDB URI:
     ```
     MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
     ```

5. **Initialize data:**
   - The `data.json` file contains sample account data
   - Ensure the file is present in the root directory

---

## 🚀 Usage

### Running the Application

**For Windows:**
```bash
python main.py
```

**For macOS:**
```bash
python main_mac.py
```

### User Workflow

1. **Login**: Enter your Account ID and PIN
2. **ATM Operations**: 
   - Check balance
   - Make deposits
   - Withdraw funds
   - Transfer money between accounts
   - View transaction history
3. **Support Chat**: Click "Contact Support" to start a live chat session with administrators
4. **Admin Access**: Login with admin credentials to access the admin panel for user management and support chat handling

### Admin Features

- Create and manage user accounts
- View and modify account balances
- Monitor transaction history
- Handle live support chat sessions
- Block/unblock user accounts

### Chat Support System

- Users can initiate support chats from the dashboard
- Real-time messaging with persistent storage in MongoDB
- Admin can respond to active chat sessions
- Sessions are managed to prevent multiple concurrent chats

---

## 🔧 Configuration

### Environment Variables
- `MONGO_URI`: MongoDB connection string (required for chat functionality)

### Data Files
- `data.json`: Contains user accounts, balances, and transaction history
- MongoDB collections: `support_chats` for chat session data

---

## 📋 Dependencies

Key dependencies include:
- `customtkinter`: Modern GUI framework
- `pymongo`: MongoDB driver for Python
- `pillow`: Image processing for UI assets
- `python-dotenv`: Environment variable management
- `CTkTable`: Table widget for admin interfaces

See `requirements.txt` for the complete list.

---

## 🏗️ Architecture

The application follows a clean, layered architecture:

- **UI Layer** (`ui_windows/`): Handles all user interface components using `customtkinter` and `CTkTable` for tables.
- **Business Logic Layer** (`models.py`): Contains the `Client` and `Admin` classes with methods for transactions and account management.
- **Data Layer** (`storage.py`): Manages JSON file operations for persistent data storage.
- **Entry Points** (`main.py`, `main_mac.py`): Platform-specific application launchers.

This separation ensures maintainability and allows for easy testing and future enhancements.

---

## ⚙️ Configuration

The application uses a JSON file (`data.json`) for data storage. No additional configuration files are required, but you can modify the data file directly for initial setup or testing.

For development, ensure Python 3.10+ is used, as the code leverages modern Python features.

---



## 📸 Screenshots

*Coming soon: Screenshots of the login screen, dashboard, and admin panel will be added here.*

---


## 👥 The Team

- **Guy Peres**
- **Tony Verin**
- **Harel Valfish**

---


## 📄 License

This project is licensed under the MIT License.
