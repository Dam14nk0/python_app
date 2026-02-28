from flask import Blueprint, jsonify

ide_bp = Blueprint("ide", __name__)


@ide_bp.post("/ide/run")
def ide_run():
    return jsonify({"message": "ide run placeholder"}), 501


@ide_bp.post("/ide/check")
def ide_check():
    return jsonify({"message": "ide check placeholder"}), 501
