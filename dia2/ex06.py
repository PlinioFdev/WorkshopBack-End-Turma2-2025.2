class Animal:
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return "Som do animal"

    def apresentar(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

class Gato(Animal):
    def falar(self):
        return "Miau!"

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Zoologico:
    def _init_(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def listar_animais(self):
        return [
            f"{animal.apresentar()} - Som: {animal.falar()}"
            for animal in self.animais
        ]

    def filtrar_por_tipo(self, tipo):
        return [
            animal for animal in self.animais
            if isinstance(animal, tipo)
        ]

def main():
    zoo = Zoologico()
    zoo.adicionar_animal(Gato("Bartolomeu", 3))
    zoo.adicionar_animal(Cachorro("Osvaldo", 5))
    zoo.adicionar_animal(Gato("Pliniozinho", 2))
    zoo.adicionar_animal(Cachorro("Tobias", 4))

    # Listar todos os animais
    todos = zoo.listar_animais()
    # Filtrar apenas gatos
    gatos = zoo.filtrar_por_tipo(Gato)
    # Filtrar apenas cachorros
    cachorros = zoo.filtrar_por_tipo(Cachorro)

    return todos, [gato.apresentar() for gato in gatos], [cachorro.apresentar() for cachorro in cachorros]

if __name__ == "__main__":
    todos, gatos, cachorros = main()
    print("Todos os animais do zoológico:")
    for item in todos:
        print(item)
    print("\nApenas os gatos:")
    for item in gatos:
        print(item)
    print("\nApenas os cachorros:")
    for item in cachorros:
        print(item)
