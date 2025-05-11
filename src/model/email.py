from src.extensions.extensions import db
from datetime import datetime

class Email(db.Model):
    def __init__(self, name, email_address, content, ip_address):
        self.name = name
        self.email_address = email_address
        self.content = content
        self.ip_address = ip_address
        self.creation_date = datetime.now()

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    email_address = db.Column(db.String, nullable=False)
    ip_address = db.Column(db.String, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "content": self.content,
            "ip_address": self.ip_address,
            "creation_date": self.creation_date
        }

    def __repr__(self):
        return f"<Email {self.creation_date} {self.id} {self.ip_address} {self.name} {self.content} {self.email_address}>"

    def __str__(self):
        return f"Email {self.creation_date} {self.id} {self.ip_address} {self.name} {self.content} {self.email_address}"