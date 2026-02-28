from flask import Blueprint, jsonify

auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/register")
def register():
    return jsonify({"message": "register endpoint placeholder"}), 501


@auth_bp.post("/login")
def login():
    return jsonify({"message": "login endpoint placeholder"}), 501


@auth_bp.get("/me")
def me():
    return jsonify({"message": "me endpoint placeholder"}), 501
