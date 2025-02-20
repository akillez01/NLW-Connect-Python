import pytest
from .eventos_repository import EventosRepository

def test_insert_eventos():
    """Testa a inserção de um evento no banco de dados"""
    event_name = "eventoTeste2"
    event_repo = EventosRepository()
    
    event_repo.insert(event_name=event_name)
    print(f"Evento '{event_name}' inserido no banco.")

def test_select_event():
    """Testa a seleção de um evento no banco de dados"""
    event_name = "eventoTeste1"
    event_repo = EventosRepository()
    
    print("Buscando evento no banco de dados...")
    event = event_repo.select_event(event_name=event_name)
    print(f"Resultado da busca: {event}")

    assert event is not None, f"Erro: Nenhum evento encontrado com o nome '{event_name}'"
    print("Evento encontrado:", event)
    print("Nome do evento:", event.nome)
