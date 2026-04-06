from pymongo import MongoClient
from datetime import datetime
import models
from ui_windows import ui_dashboard
from ui_windows import ui_admin_login
import storage
import json
import os
import sys
import certifi
from dotenv import load_dotenv
load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__)) 
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

class SupportManager:
    def __init__(self):
        cr = certifi.where()
        mongoconnectionstring = os.getenv("MONGO_URI")
        self.client = MongoClient(mongoconnectionstring, tlsCAFile=cr)
        self.db = self.client["ArgumentCapitalChatDB"]
        self.chats = self.db["support_chats"]

    def _get_next_session_id(self):
        """Finds the last session number and increments it."""
        last_session = self.chats.find_one(sort=[("_id", -1)])
        if not last_session or "session_id" not in last_session:
            return "session_1"
        
        # extract number from "session_N"
        try:
            current_num = int(last_session["session_id"].split("_")[1])
            return f"session_{current_num + 1}"
        except (IndexError, ValueError):
            return "session_1"

    def try_start_chat(self, user_id):
        """Checks if any session is currently busy."""
        active_session = self.chats.find_one({"is_busy": True})
        
        if active_session:
            # if the busy session belongs to this user, it lets them back in!
            if active_session.get("current_user_id") == user_id:
                return True, active_session["session_id"]
            return False, "Support is currently busy with another client."
        
        # this means no one is busy, create a brand new incremented session
        new_id = self._get_next_session_id()
        self.chats.insert_one({
            "session_id": new_id,
            "is_busy": True,
            "current_user_id": user_id,
            "messages": [],
            "created_at": datetime.now()
        })
        return True, new_id

    def send_message(self, session_id, sender_id, text):
        self.chats.update_one(
            {"session_id": session_id},
            {"$push": {"messages": {
                "sender": sender_id,
                "text": text,
                "timestamp": datetime.now().strftime("%H:%M")
            }}}
        )

    def get_messages(self, session_id):
        session = self.chats.find_one({"session_id": session_id})
        return session.get("messages", []) if session else []

    def end_chat(self, session_id):
        """Sets is_busy to False so the next session_id can be generated later."""
        self.chats.update_one(
            {"session_id": session_id},
            {"$set": {"is_busy": False}}
        )