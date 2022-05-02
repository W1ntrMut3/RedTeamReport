from flask import Blueprint

generate = Blueprint("generate", __name__, url_prefix="/api/v1/generate")

@generate.post('/<int:engagement_id>/generate')
@jwt_required()
def register():
    return "User Created"


@generate.get("/<int:document_id>/download")
@jwt_required()
def me():
    return {"user":"me"}