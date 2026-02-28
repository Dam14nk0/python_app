from flask import Blueprint, jsonify

courses_bp = Blueprint("courses", __name__)


@courses_bp.get("/courses")
def list_courses():
    return jsonify({"message": "courses list placeholder"}), 501


@courses_bp.get("/courses/<slug>")
def course_detail(slug: str):
    return jsonify({"message": f"course detail placeholder: {slug}"}), 501


@courses_bp.get("/courses/<slug>/day/<int:day_number>")
def course_day(slug: str, day_number: int):
    return jsonify({"message": f"lesson placeholder: {slug} day {day_number}"}), 501
