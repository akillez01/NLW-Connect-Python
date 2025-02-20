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
    
@pytest.mark.skip("Insert in db")
def test_select_subscriber():
    email = "email22@email.com"
    evento_id = 2

    db_url = "sqlite:///schema.db"  # Adicionado
    subs_repo = SubscribersRepository(db_url)

    # Tenta chamar o método
    resp = subs_repo.select_subscriber(email, evento_id)
    print(resp.nome)
