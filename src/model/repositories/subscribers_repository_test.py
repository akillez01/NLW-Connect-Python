import pytest
from src.model.repositories.subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in db")
def test_insert():
    subscriber_info = {
        "nome": "Teste",
        "email": "email22@email.com",
        "evento_id": 2
    }
    db_url = "sqlite:///schema.db"  # Adicionado
    subs_repo = SubscribersRepository(db_url)
    subs_repo.insert(subscriber_info)
    
@pytest.mark.skip("Insert in DB")
def test_select_subscriber():
    email = "email22@email.com"
    evento_id = 2

    db_url = "sqlite:///schema.db"  # Adicionado
    subs_repo = SubscribersRepository()

    # Tenta chamar o método
    resp = subs_repo.select_subscriber(email, evento_id)
    print(resp.nome)
    
def test_ranking():
    evento_id = 8
    subs_repo = SubscribersRepository()
    resp = subs_repo.get_ranking(evento_id)
    print()
    
    for elem in resp:
        print(f"Link: {elem.link}, total de inscritos: {elem.total}")
