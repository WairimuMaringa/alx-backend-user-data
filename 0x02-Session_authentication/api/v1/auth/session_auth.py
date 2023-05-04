#!/usr/bin/env python3
"""
Module sessionauth
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """Sesh auth"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create sesh for user_id
        """
        if user_id is None or type(user_id) is not str:
            return None

        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Return userid based on a seshid
        """
        if session_id is None or\
                type(session_id) is not str:
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Return user instance
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """
        Logs out user
        """
        if request is None:
            return False

        cookie = self.session_cookie(request)

        if cookie is None or\
                self.user_id_for_session_id(cookie) is None:
            return False

        del self.user_id_by_session_id[cookie]

        return True
