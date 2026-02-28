import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app import create_app


def test_workspace_files_crud_and_fixtures_endpoint():
    app = create_app()
    client = app.test_client()

    get_resp = client.get('/api/workspace/files?user_id=u1&course_slug=python-for-pentesters')
    assert get_resp.status_code == 200
    assert isinstance(get_resp.get_json()['files'], list)

    save_resp = client.post('/api/workspace/files', json={
        'user_id': 'u1',
        'course_slug': 'python-for-pentesters',
        'path': 'outputs/nmap.txt',
        'content': 'PORT 22 open',
    })
    assert save_resp.status_code == 200
    assert any(f['path'] == 'outputs/nmap.txt' for f in save_resp.get_json()['files'])

    fixtures_resp = client.get('/api/fixtures?tool=nmap')
    assert fixtures_resp.status_code == 200
    payload = fixtures_resp.get_json()
    assert payload['count'] >= 1
