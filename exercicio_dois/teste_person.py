import pytest
from person import Email, Person, PersonDAO

def test_email_valid():
    # Testa um email válido
    email = Email(1, "joao.silva@example.com")
    assert email.email == "joao.silva@example.com"

def test_email_invalid():
    # Testa um email inválido
    with pytest.raises(ValueError):
        Email(1, "joao.silva@com")

def test_person_valid():
    # Testa uma pessoa com dados válidos
    emails = [Email(1, "joao.silva@example.com")]
    person = Person(1, "João Silva", 30, emails)
    person_dao = PersonDAO()
    assert person_dao.isValidToInclude(person) == []

def test_person_invalid_name():
    # Testa uma pessoa com nome inválido
    emails = [Email(1, "joao.silva@example.com")]
    person = Person(1, "João123 Silva", 30, emails)
    person_dao = PersonDAO()
    assert person_dao.isValidToInclude(person) == ["Nome inválido."]

def test_person_invalid_age():
    # Testa uma pessoa com idade inválida
    emails = [Email(1, "joao.silva@example.com")]
    person = Person(1, "João Silva", 201, emails)
    person_dao = PersonDAO()
    assert person_dao.isValidToInclude(person) == ["Idade inválida."]

def test_person_no_emails():
    # Testa uma pessoa sem emails
    person = Person(1, "João Silva", 30, [])
    person_dao = PersonDAO()
    assert person_dao.isValidToInclude(person) == ["Pelo menos um email é necessário."]
