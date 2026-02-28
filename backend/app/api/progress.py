from flask import Blueprint, jsonify

progress_bp = Blueprint("progress", __name__)


@progress_bp.get("/progress/<slug>")
def get_progress(slug: str):
    return jsonify({"message": f"progress placeholder: {slug}"}), 501


@progress_bp.post("/progress/task")
def complete_task():
    return jsonify({"message": "task completion placeholder"}), 501


@progress_bp.post("/progress/complete-day")
def complete_day():
    return jsonify({"message": "complete day placeholder"}), 501
