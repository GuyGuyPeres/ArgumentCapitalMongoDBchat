<div align="center">

![Banner](https://placehold.co/900x200/0d1117/ffffff?text=Argument+Capital+ATM&font=montserrat)

# 🏦 Argument Capital ATM

### A full-featured desktop ATM simulator with live MongoDB-powered chat support

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![customtkinter](https://img.shields.io/badge/customtkinter-5.2.2-1f6aa5?style=for-the-badge)](https://github.com/TomSchimansky/CustomTkinter)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![pymongo](https://img.shields.io/badge/pymongo-4.16.0-47A248?style=for-the-badge)](https://pypi.org/project/pymongo/)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)](https://github.com/GuyGuyPeres/ArgumentCapitalMongoDBchat/pulls)

<a href="https://ibb.co/gZvyhtB7"><img src="https://i.ibb.co/r2bkN51t/image.png" alt="image" border="0"></a>

</div>

---

## 📖 Table of Contents
- [Tech Stack](#-tech-stack)
- [Key Features](#-key-features)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Architecture](#-architecture)
- [License](#-license)

---

## 🛠 Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| Language | Python | 3.10+ |
| GUI Framework | customtkinter | 5.2.2 |
| GUI Extras | CTkTable, pywinstyles | 1.1 / 1.8 |
| Database — Chat | MongoDB Atlas | pymongo 4.16.0 |
| Database — Accounts | JSON (data.json) | — |
| Env Management | python-dotenv | 1.2.2 |
| Image Processing | Pillow | 12.2.0 |
| SSL Certificates | certifi | 2021.5.30 |
| Testing | pytest | 9.0.2 |

---

## ✨ Key Features

- **PIN-Based Authentication** — Secure login for both users and admins with automatic account blocking after repeated failed attempts, preventing brute-force access.
- **Full ATM Operations** — Deposit, withdraw, and transfer funds between accounts with overdraft protection and real-time balance updates after every transaction.
- **Complete Transaction History** — Every financial operation is logged with type, direction, amount, old/new balance, and a timestamp for full auditability.
- **Admin Control Panel** — Administrators can create, search, block, unblock, promote, and permanently delete user accounts from a dedicated dashboard.
- **Live MongoDB Chat Support** — Users open a real-time support session directly from the dashboard; messages persist in MongoDB Atlas and admins respond from the admin panel.
- **Session-Managed Chat Queue** — The support engine enforces one active session at a time per slot, preventing chat collisions and allowing clean session handoffs.
- **Dual Data Persistence** — Account and transaction data live in a local JSON file for speed; chat sessions live in MongoDB for cloud persistence — each storage layer optimised for its workload.
- **Modular Layered Architecture** — UI, business logic, JSON storage, and MongoDB chat are fully decoupled layers, making each independently testable and replaceable.
- **Cross-Platform Desktop App** — Dedicated entry points (`main.py` for Windows, `main_mac.py` for macOS) with platform-aware UI and native styling via `pywinstyles`.

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [MongoDB Atlas account](https://www.mongodb.com/cloud/atlas) or a local MongoDB instance
- Display scaling set to **100%** — the UI is calibrated for 1:1 scaling; other values will misalign elements

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GuyGuyPeres/ArgumentCapitalMongoDBchat.git
   cd ArgumentCapitalMongoDBchat
   ```

2. **Create and activate a virtual environment:**

   macOS / Linux:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**

   Create a `.env` file in the project root:
   ```env
   MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority
   ```

   > ⚠️ Never commit your `.env` file. It contains your MongoDB credentials. Confirm `.env` is listed in `.gitignore` before your first push.

5. **Set up MongoDB:**
   - In MongoDB Atlas, create a database named `ArgumentCapitalChatDB`
   - Inside it, create a collection named `support_chats`
   - Whitelist your IP address under **Network Access**

6. **Verify sample data:**
   - Confirm `data.json` is present in the project root — it seeds the initial user accounts and is required at startup

<details>
<summary>🔧 <b>Troubleshooting</b></summary>

- **`ServerSelectionTimeoutError` on startup** — Your `MONGO_URI` in `.env` is incorrect, or your current IP address is not whitelisted in MongoDB Atlas → Security → Network Access.
- **`ModuleNotFoundError`** — Your virtual environment is not activated. Run `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows), then re-run `pip install -r requirements.txt`.
- **UI elements misaligned or oversized** — Open OS display settings and set scaling to exactly **100%**, then restart the application.
- **`FileNotFoundError: data.json`** — The local JSON database is missing. Restore `data.json` from the repository. Do not delete this file while the app is running.
- **`dotenv` not loading** — Ensure the `.env` file is in the project root (same directory as `main.py`) and has no syntax errors.

</details>

### Run the App

**Windows:**
```bash
python main.py
```

**macOS:**
```bash
python main_mac.py
```

The desktop window launches immediately. No server or browser required.

### Run Tests

```bash
pytest
```

---

## 💡 Usage

### User Workflow

1. **Login** — Enter your Account ID and PIN. After too many wrong attempts the account is automatically blocked.
2. **Dashboard** — All ATM operations are available from the main dashboard:

| Action | What it does |
|--------|-------------|
| Check Balance | Displays current account balance |
| Deposit | Adds funds; rejects negative amounts |
| Withdraw | Deducts funds; blocks if balance is insufficient |
| Transfer | Moves funds to another account by ID |
| Transaction History | Shows every past operation with timestamps |
| Contact Support | Opens a live chat session with an admin |

3. **Support Chat** — Click **Contact Support** to start a session. Type messages in real time and wait for an admin response. Close the window to end the session.

### Admin Workflow

Login with admin credentials to reach the **Admin Panel**:

| Feature | Description |
|---------|-------------|
| View All Users | Table of every non-admin account with balances and status |
| Create Account | Register a new user with username, PIN, and starting balance |
| Find Account | Search any account by ID |
| Block / Unblock | Toggle account access without deleting the record |
| Promote to Admin | Elevate a user account to admin privileges |
| Delete Account | Permanently remove an account from the system |
| Support Chat | Receive and reply to active user chat sessions in real time |

### Chat Support System

The support engine (`support_manager.py`) manages sessions stored in MongoDB:

```json
{
  "session_id": "session_1",
  "is_busy": true,
  "current_user_id": 103,
  "messages": [
    { "sender": 103, "text": "Hello, I need help.", "timestamp": "14:32" }
  ],
  "created_at": "<datetime>"
}
```

- One active session slot at a time prevents chat collisions
- Users who already have an active session re-enter it on reconnect
- Admins end the session from the admin panel, freeing the slot for the next user

---

## 🏗 Architecture

### Folder Structure

```text
📁 ArgumentCapitalMongoDBchat/
├── 📄 main.py                    # Windows entry point
├── 📄 main_mac.py                # macOS entry point
├── 📄 models.py                  # Client & Admin domain models + business logic
│                                 #   ↳ Client: deposit, withdraw, transfer, check_pin, change_pin
│                                 #   ↳ Admin:  create_client, block, promote, delete, find_account
├── 📄 storage.py                 # JSON persistence layer
│                                 #   ↳ all_clients(), save_clients(), transaction_format()
├── 📄 data.json                  # Local data store — accounts & transaction history
├── 📄 requirements.txt           # Pinned Python dependencies
├── 📄 .env                       # MONGO_URI secret (never committed)
└── 📁 ui_windows/                # All UI screens
    ├── 📄 support_manager.py     # MongoDB chat engine — session creation, messaging, teardown
    ├── 📄 ui_admin_login.py      # Admin authentication screen
    ├── 📄 ui_admin_panel.py      # Admin dashboard: user table + live chat interface
    ├── 📄 ui_admin_user_table.py # Detailed user management table view
    ├── 📄 ui_dashboard.py        # User dashboard: ATM operations + chat entry point
    ├── 📄 test_final_ui.py       # Windows UI integration tests
    └── 📄 test_ui_mac.py         # macOS UI integration tests
```

### Request Flow

```
User Input (GUI event)
        ↓
UI Layer  ── ui_dashboard.py / ui_admin_panel.py
        ↓
Business Logic ── models.py  (Client / Admin methods)
        ↓                          ↓
storage.py                 support_manager.py
(read/write data.json)     (MongoDB Atlas — ArgumentCapitalChatDB.support_chats)
        ↓                          ↓
     JSON file               MongoDB document
        ↓                          ↓
        └──────────┬───────────────┘
                   ↓
          UI update / error feedback
               ↑
  Error handlers intercept at each layer boundary
```

## 👥 The Team

| Name | Role |
|------|------|
| **Guy Peres** | Developer |
| **Tony Verin** | Developer |
| **Harel Valfish** | Developer |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

Made with ☕, `customtkinter`, and way too many MongoDB queries

⭐ **If this project helped you, consider giving it a star!** ⭐

Built with 💻 by [Guy Peres](https://github.com/GuyGuyPeres) · [Tony Verin](https://github.com/) · [Harel Valfish](https://github.com/)

</div>
