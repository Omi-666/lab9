
def testy():

    print("\nZad1\n")
    p1 = Student("Dominika","Banasiak",19292,"IIS")
    
    print(p1.imie)
    print(p1.nazwisko)
    #print(p1.__nr_indeksu)
    print(p1.kierunek)
    
    print(p1)
    
    print("\nZad2\n")

    p2 = Student("Krzysztof","Kowalski",15335,"AWF")
    
    print(p1.__lt__(p2))
    print(p1.__eq__(p2))
    
    print("\nZad3\n")

    p3 = Student("Amelia","Nowak",11223,"IIS")
    
    print("Licznik: %s"%(p3.getLicznik()))
    
    print("\nZad4\n")

    p4 = StudentInformatyki("Dominika","Banasiak",19292,"IIS","Grafika")
    print(p4)
    
    print(p4.specjalnosc)
    pass

class Student():
    __licznik = 0
    
    def __init__(self, imie, nazwisko, nr_indeksu, kierunek):
        Student.__licznik += 1
        self.imie = imie
        self.nazwisko = nazwisko
        self.__nr_indeksu = nr_indeksu
        self.kierunek = kierunek
        
    def getLicznik(self):
        return self.__licznik
        
    def __lt__(self,other):
        if self.nazwisko < other.nazwisko:
            return True
        else:
            return False
        
    def __eq__(self,other):
        if self.nazwisko == other.nazwisko:
            return True
        else:
            return False
    
    def __str__(self):
        return "Imie: %s\nnazwisko: %s\nnr ideksu: %s\nkierunek: %s"%(self.imie, self.nazwisko, self.__nr_indeksu, self.kierunek)

class StudentInformatyki(Student):
    def __init__(self, imie, nazwisko, nr_indeksu, kierunek, specjalnosc):
        super(StudentInformatyki,self).__init__(imie, nazwisko, nr_indeksu, kierunek)
        self.kierunek = "IIS"
        self.specjalnosc = specjalnosc

if __name__ == "__main__":
    testy()
