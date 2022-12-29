from flask import Blueprint, request
from webargs.flaskparser import parser
from marshmallow import Schema, fields
from ..schemas import model
from .. import impl

bp = Blueprint('spacecrafts', __name__)


@bp.route('/spacecrafts/<spacecraftId>', methods=['get'])
def GetSpacecraftId(spacecraftId):

    options = {}
    options["spacecraftId"] = spacecraftId

    return impl.spacecrafts.GetSpacecraftId(options)


@bp.route('/spacecrafts/<spacecraftId>', methods=['put'])
def PutSpacecraftId(spacecraftId):

    options = {}
    options["spacecraftId"] = spacecraftId

    return impl.spacecrafts.PutSpacecraftId(options)
