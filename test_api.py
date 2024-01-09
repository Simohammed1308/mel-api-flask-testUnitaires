from conftest import client


def test_should_status_code_ok(client):
    response = client.get('/index')
    assert response.status_code == 200

def test_should_return_welcome(client):
    response = client.get('/index')
    data = response.data.decode() #Permet de décoder la data dans la requête
    assert data == 'Welcome to my Flask API!'

def test_should_return_score(client):
    response = client.get('/score_min/')
    data = response.data.decode() #Permet de décoder la data dans la requête
    data = data.replace('\n','').replace(' ','')
    compa = '{"score_min":0.55}'
    assert data == compa
 