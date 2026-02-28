from __future__ import annotations

from datetime import datetime, timezone

from ..extensions import mongo_client

_MEM_DB: dict[tuple[str, str], dict] = {}


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _default_doc(user_id: str, course_slug: str) -> dict:
    return {
        "user_id": user_id,
        "course_slug": course_slug,
        "files": [],
        "last_modified": _utc_now(),
    }


def get_user_files(user_id: str, course_slug: str) -> dict:
    if mongo_client:
        db = mongo_client.get_default_database()
        doc = db.user_files.find_one({"user_id": user_id, "course_slug": course_slug}, {"_id": 0})
        return doc or _default_doc(user_id, course_slug)

    key = (user_id, course_slug)
    return _MEM_DB.get(key, _default_doc(user_id, course_slug))


def save_user_files(user_id: str, course_slug: str, files: list[dict]) -> dict:
    document = {
        "user_id": user_id,
        "course_slug": course_slug,
        "files": files,
        "last_modified": _utc_now(),
    }

    if mongo_client:
        db = mongo_client.get_default_database()
        db.user_files.replace_one({"user_id": user_id, "course_slug": course_slug}, document, upsert=True)
        return document

    _MEM_DB[(user_id, course_slug)] = document
    return document
