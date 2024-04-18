class Email:
    def __init__(self, id, email):
        self.id = id
        self.email = email
        if not self.is_valid_email():
            raise ValueError("Email inválido.")

    def is_valid_email(self):
        email = self.email.strip()
        parts = email.split('@')
        if len(parts) != 2:
            return False
        
        local_part, domain_part = parts
        if len(local_part) == 0 or '.' not in domain_part:
            return False
        
        domain_parts = domain_part.split('.')
        if len(domain_parts) < 2 or not all(len(part) > 0 for part in domain_parts):
            return False
        
        # Verifique a extensão do domínio: pelo menos 2 caracteres alfabéticos
        if not (2 <= len(domain_parts[-1]) <= 6) or not domain_parts[-1].isalpha():
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
        
        name_parts = self.name.split()
        if len(name_parts) < 2 or not all(part.isalpha() for part in name_parts):
            errors.append("Nome inválido.")
        

        if not (1 <= self.age <= 200):
            errors.append("Idade inválida.")
        
        if not self.emails:
            errors.append("Pelo menos um email é necessário.")
        
        return errors


class PersonDAO:
    def save(self, person):
        print(f"Person {person.name} saved successfully.")
    
    def isValidToInclude(self, person):
        return person.isValidToInclude()
