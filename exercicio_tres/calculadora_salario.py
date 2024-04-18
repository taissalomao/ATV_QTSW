from enum import Enum

class Cargo(Enum):
    DESENVOLVEDOR = "DESENVOLVEDOR"
    DBA = "DBA"
    TESTADOR = "TESTADOR"
    GERENTE = "GERENTE"

def calcular_salario_liquido(cargo, salario_base):
    if cargo == Cargo.DESENVOLVEDOR:
        if salario_base >= 3000:
            desconto = 0.20
        else:
            desconto = 0.10
    elif cargo == Cargo.DBA or cargo == Cargo.TESTADOR:
        if salario_base >= 2000:
            desconto = 0.25
        else:
            desconto = 0.15
    elif cargo == Cargo.GERENTE:
        if salario_base >= 5000:
            desconto = 0.30
        else:
            desconto = 0.20
    
    salario_liquido = salario_base * (1 - desconto)
    return salario_liquido
