studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfer):
    return [int(sum(cijfers) / len(cijfers)) for cijfers in studentencijfer]

def gemiddelde_van_alle_studenten(studentencijfer):
    return sum(gemiddelde_per_student(studentencijfer)) / len(gemiddelde_per_student(studentencijfer))

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))