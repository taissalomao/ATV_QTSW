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

def test_email_no_at():
    with pytest.raises(ValueError):
        Email(1, "joao.silva.com")

def test_email_multiple_ats():
    with pytest.raises(ValueError):
        Email(1, "joao@silva@example.com")

def test_email_no_domain():
    with pytest.raises(ValueError):
        Email(1, "joao.silva@")

def test_person_name_single_part():
    emails = [Email(1, "joao.silva@example.com")]
    person = Person(1, "João", 30, emails)
    person_dao = PersonDAO()
    assert person_dao.isValidToInclude(person) == ["Nome inválido."]

def test_person_name_non_alpha():
    emails = [Email(1, "joao.silva@example.com")]
    person = Person(1, "João123 Silva", 30, emails)
    person_dao = PersonDAO()
    assert person_dao.isValidToInclude(person) == ["Nome inválido."]

def test_person_dao_save():
    emails = [Email(1, "joao.silva@example.com")]
    person = Person(1, "João Silva", 30, emails)
    person_dao = PersonDAO()
    person_dao.save(person)


def test_person_negative_age():
    # Testa uma pessoa com idade negativa
    emails = [Email(1, "joao.silva@example.com")]
    person = Person(1, "João Silva", -1, emails)
    person_dao = PersonDAO()
    assert person_dao.isValidToInclude(person) == ["Idade inválida."]

def test_person_age_zero():
    # Testa uma pessoa com idade zero
    emails = [Email(1, "joao.silva@example.com")]
    person = Person(1, "João Silva", 0, emails)
    person_dao = PersonDAO()
    assert person_dao.isValidToInclude(person) == ["Idade inválida."]

def test_email_with_uncommon_extension():
    # Teste com extensão ausente ou incomum
    with pytest.raises(ValueError):
        Email(1, "joao.silva@example")
    with pytest.raises(ValueError):
        Email(1, "joao.silva@example.c")

def test_email_with_long_domain_extension():
    with pytest.raises(ValueError):
        Email(1, "joao.silva@example.abcdefghi")

def test_email_with_incomplete_domain():
    with pytest.raises(ValueError):
        Email(1, "joao.silva@example")  

def test_email_with_empty_domain_part():
    with pytest.raises(ValueError):
        Email(1, "joao.silva@.com")  



