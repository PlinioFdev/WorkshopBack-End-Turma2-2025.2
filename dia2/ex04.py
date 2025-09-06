class Animal:
    def falar(self):
        return "Som do animal"
    
class Gato(Animal):
    def falar(self):
        return "Miau!"
    
class Cachorro(Animal):
    def falar(self):
        return "Au au!"
    
def fala_animal(a: Animal):
    return a.falar()
    
def main():
    user = str(input("Digite G para gato e C para cachorro: ")).upper().strip()
    if user == "G":
        g = Gato()
        print(fala_animal(g))
    elif user == "C":
        c = Cachorro()
        print(fala_animal(c))
    else:
        print("Animal não detectado! ")
    
if __name__ == "__main__":
    main()
