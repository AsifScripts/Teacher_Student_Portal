def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_login_redirect(client):
    response = client.get('/dashboard')
    assert response.status_code == 302
