from flask import Blueprint

generate = Blueprint("generate", __name__, url_prefix="/api/v1/generate")


# Here I need to get all of the data that I need to generate a report
# order it in a way that each issue cascades from high (first) to low (last) in priority of severity
# I then need to output it to the document using a template
# I need the template to be able to output entire "issue" chunks mutliple times
#
#
#
#

@generate.post('/<int:engagement_id>/generate')
@jwt_required()
def register():
    return "User Created"


@generate.get("/<int:document_id>/download")
@jwt_required()
def me():
    return {"user":"me"}