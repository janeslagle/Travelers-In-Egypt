# TODO
# Create the blueprint for nile travelogues. Connect it to the
# main database blueprint, db_blueprint, in the v1 __init__.py file

from flask import Blueprint, jsonify
from models import cursor

nile_travelogues_blueprint = Blueprint('nile-travelogues', __name__)

@nile_travelogues_blueprint.route("/nile-travelogues")
def getBoatPassengers():
    cursor.execute("SELECT * FROM Publications")
    version = cursor.fetchall()
    
    if len(version):
        columns = [desc[0] for desc in cursor.description]
        version = [dict(zip(columns, row)) for row in version]
        return jsonify(version)
    else:
        return "No related information"