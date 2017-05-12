import pytest

# from website import views

pytestmark = pytest.mark.django_db


@pytest.mark.django_db(transaction=True)
def test_home_page(client):

    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_contact(client):
    response = client.post(
        '/website/subscribe/', {
            'email': 'exampl@gmail.com'
        },
                          )
    assert response.get('location') == '/website/success/'


def test_venue_renders_correctly(client):
    response = client.get('/website/venue')
    assert response.status_code == 301
