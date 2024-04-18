class Email:
    def __init__(self, id, email):
        self.id = id
        self.email = email
        # Valida o formato do email
        if not self.is_valid_email():
            raise ValueError("Email inválido.")

    def is_valid_email(self):
        # Verifica o formato "____@____.____" com pelo menos 1 caractere em cada parte
        parts = self.email.split('@')
        if len(parts) != 2:
            return False
        
        local_part, domain_part = parts
        if len(local_part) == 0 or '.' not in domain_part:
            return False
        
        domain, extension = domain_part.split('.')
        if len(domain) == 0 or len(extension) == 0:
            return False
        
        return True


class Person:
    def __init__(self, id, name, age, emails):
        self.id = id
        self.name = name
        self.age = age
        self.emails = emails

    def isValidToInclude(self):
        errors = []
        
        # Verifica se o nome tem pelo menos duas partes e apenas letras
        name_parts = self.name.split()
        if len(name_parts) < 2 or not all(part.isalpha() for part in name_parts):
            errors.append("Nome inválido.")
        
        # Verifica se a idade está no intervalo [1, 200]
        if not (1 <= self.age <= 200):
            errors.append("Idade inválida.")
        
        # Verifica se há pelo menos um email
        if not self.emails:
            errors.append("Pelo menos um email é necessário.")
        
        return errors


class PersonDAO:
    def save(self, person):
        print(f"Person {person.name} saved successfully.")
    
    def isValidToInclude(self, person):
        return person.isValidToInclude()
