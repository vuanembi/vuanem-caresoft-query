from .auth_service import create_authorization_url


def test_create_authorization_url():
    url = create_authorization_url()
    assert url
