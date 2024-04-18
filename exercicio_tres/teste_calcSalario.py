import pytest
from calculadora_salario import calcular_salario_liquido, Cargo

def test_calcular_salario_liquido_desenvolvedor():
    # Testa desconto de 20% para desenvolvedor com salário >= 3.000
    salario_base = 4000.00
    salario_esperado = salario_base * 0.80  # 20% de desconto
    assert calcular_salario_liquido(Cargo.DESENVOLVEDOR, salario_base) == salario_esperado
    
    # Testa desconto de 10% para desenvolvedor com salário < 3.000
    salario_base = 2500.00
    salario_esperado = salario_base * 0.90  # 10% de desconto
    assert calcular_salario_liquido(Cargo.DESENVOLVEDOR, salario_base) == salario_esperado

def test_calcular_salario_liquido_dba():
    # Testa desconto de 25% para DBA com salário >= 2.000
    salario_base = 2500.00
    salario_esperado = salario_base * 0.75  # 25% de desconto
    assert calcular_salario_liquido(Cargo.DBA, salario_base) == salario_esperado
    
    # Testa desconto de 15% para DBA com salário < 2.000
    salario_base = 1500.00
    salario_esperado = salario_base * 0.85  # 15% de desconto
    assert calcular_salario_liquido(Cargo.DBA, salario_base) == salario_esperado

def test_calcular_salario_liquido_testador():
    # Testa desconto de 25% para testador com salário >= 2.000
    salario_base = 2200.00
    salario_esperado = salario_base * 0.75  # 25% de desconto
    assert calcular_salario_liquido(Cargo.TESTADOR, salario_base) == salario_esperado
    
    # Testa desconto de 15% para testador com salário < 2.000
    salario_base = 1800.00
    salario_esperado = salario_base * 0.85  # 15% de desconto
    assert calcular_salario_liquido(Cargo.TESTADOR, salario_base) == salario_esperado

def test_calcular_salario_liquido_gerente():
    # Testa desconto de 30% para gerente com salário >= 5.000
    salario_base = 7000.00
    salario_esperado = salario_base * 0.70  # 30% de desconto
    assert calcular_salario_liquido(Cargo.GERENTE, salario_base) == salario_esperado
    
    # Testa desconto de 20% para gerente com salário < 5.000
    salario_base = 4500.00
    salario_esperado = salario_base * 0.80  # 20% de desconto
    assert calcular_salario_liquido(Cargo.GERENTE, salario_base) == salario_esperado
