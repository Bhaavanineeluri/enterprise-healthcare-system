from sqlalchemy.orm import Session as DBSession

from models.session import Session


class SessionRepository:

    def __init__(
        self,
        db: DBSession
    ):
        self.db = db

    def create(
        self,
        session: Session
    ):

        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)

        return session

    def get_active_session(
        self,
        access_token: str
    ):

        return (
            self.db.query(Session)
            .filter(
                Session.access_token == access_token,
                Session.is_active == True
            )
            .first()
        )

    def deactivate(
        self,
        session: Session
    ):

        session.is_active = False

        self.db.commit()

        return session