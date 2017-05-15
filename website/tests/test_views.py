import pytest

pytestmark = pytest.mark.django_db


@pytest.mark.django_db(transaction=True)
def test_home_page(client):

    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_subscribe(client):
    response = client.post(
        '/subscribe/', {
            'email': 'exampl@gmail.com'
        },
                          )
    assert response.get('location') == '/success/'


def test_venue_renders_correctly(client):
    response = client.get('/website/venue')
    assert response.status_code == 301


def test_contact(client):
    with pytest.raises(ValueError):
        response = client.post(
            '/contact/', {
                'name': 'Example User',
                'company': 'Company',
                'email': 'user@example.com',
                'message': 'Hello World'
            }
        )

        # assert 'thanks.html' in response.templates
