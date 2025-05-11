from flask import Blueprint, request

from src.messages.response_message import ResponseMessage
from src.extensions.extensions import db
import logging

from src.model.access_log_record import AccessLogRecord

access_log_blueprint = Blueprint("access_log_blueprint", __name__, url_prefix="/api/v1/accesslog")

logger = logging.getLogger(__name__)

@access_log_blueprint.route("/new", methods=['GET'])
def create_new_record():
    if request.headers.getlist("X-Forwarded-For"):
        client_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        client_ip = request.remote_addr
    new_record = AccessLogRecord(client_ip)
    db.session.add(new_record)
    db.session.commit()

    response_message = ResponseMessage("access record created successfully", 201)
    return response_message.create_response_message()
