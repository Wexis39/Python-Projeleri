class Ogrenciler:
    def __init__(self, name, surname, no, exam1, exam2, final):
        self.name = name
        self.surname = surname
        self.no = no
        self.exam1 = exam1
        self.exam2 = exam2
        self.final = final

students = []

def ort(exam1_input, exam2_input, final_input):
    return int(((exam1_input * 20) / 100) + ((exam2_input * 20) / 100) + ((final_input * 60) / 100))

while True:
    veri = int(input("Öğrenci eklemek için 1\nÖğrenci verilerini görmek için 2\nSeçiminiz: "))
    if veri == 2:
        for student in students:
            print("*"*20)
            print("Öğrenci adı:", student.name,"\nÖğrenci soyadı:", student.surname,"\nÖğrenci no:", student.no,"\n1. Sınav notu:", student.exam1,"\n2. Sınav notu: ", student.exam2,"\nFinal notu:", student.final)
            print("Ortalaması: ", ort(student.exam1, student.exam2, student.final))
        print("*" * 20)
    elif veri == 1:
        name_input = input("İsim: ")
        surname_input = input("Soyisim: ")
        no_input = input("No: ")
        exam1_input = int(input("1. Sınav notu: "))
        exam2_input = int(input("2. Sınav notu: "))
        final_input = int(input("Final notu: "))
        students.append(Ogrenciler(name_input, surname_input, no_input, exam1_input, exam2_input, final_input))
        print("Öğrenci eklendi...")
        print("*" * 20)
    else:
        print("1 veya 2'yi seçiniz")
        print("*" * 20)
