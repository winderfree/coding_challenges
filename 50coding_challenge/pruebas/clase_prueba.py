class Persona:
    def __init__(self, name) -> str:
        self.name = name
        self.languages = []

    def add_languages(self, language):
        self.languages.append(language)

if "__main__" == __name__:
    es = Persona("Juan Casado Luna")
    es.add_languages("Español")
    es.add_languages("Ïngles")
    print(f'{es.name}')
    print(f'Lenguajes: {es.languages}'  )