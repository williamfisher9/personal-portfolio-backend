from flask import request
from datetime import datetime

from src.extensions.extensions import db


class AccessLogRecord(db.Model):
    def __init__(self, ip_address):
        self.creation_date = datetime.now()
        self.ip_address = ip_address

    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String, nullable=False)
    creation_date =  db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "ip_address": self.ip_address,
            "creation_date": self.creation_date
        }

    def __repr__(self):
        return f"<AccessLogRecord {self.creation_date} {self.id} {self.ip_address}>"

    def __str__(self):
        return f"AccessLogRecord {self.creation_date} {self.id} {self.ip_address}"
