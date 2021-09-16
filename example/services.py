import logging
import sqlite3
from typing import Dict

from mypy_boto3_s3  import S3Client

class BaseService:

    def __init__(self)-> None:
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )

class UserService(BaseService):

    def __init__(self, db: sqlite3.Connection) -> None:
        self.db = db
        super().__init__()

    def get_user(self, email: str) -> Dict[str,str] :
        self.logger.info(f"User {email} has been found in the database")

        return {'email': email, 'password_hash': '...'}
