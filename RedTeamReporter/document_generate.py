from flask import Blueprint

generate = Blueprint("generate", __name__, url_prefix="/api/v1/generate")

@generate.post('/register')
def register():
    return "User Created"


@generate.get("/me")
def me():
    return {"user":"me"}