from flask import Blueprint, jsonify

admin_bp = Blueprint("admin", __name__)


@admin_bp.post("/admin/module")
def create_module():
    return jsonify({"message": "create module placeholder"}), 501


@admin_bp.post("/admin/lesson")
def create_lesson():
    return jsonify({"message": "create lesson placeholder"}), 501


@admin_bp.put("/admin/lesson/<lesson_id>")
def update_lesson(lesson_id: str):
    return jsonify({"message": f"update lesson placeholder: {lesson_id}"}), 501
