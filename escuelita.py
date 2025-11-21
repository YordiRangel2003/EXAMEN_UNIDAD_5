def escuelita_sistema():
    print("\n>>>>>>>>>> Sistema de Escuelita >>>>>>>>>>\n")
    estudiantes = int(input("Ingrese el número de estudiantes: "))
    materias = int(input("Ingrese el número de materias: "))

    calificaciones = []
    for i in range(estudiantes):
        fila = []
        print(f"\n==== Capturando calificaciones del estudiante {i+1} ====")
        for j in range(materias):
            cal = float(input(f"Calificación de la materia {j+1}: "))
            fila.append(cal)
        calificaciones.append(fila)

    print("\n>>>>>>>>>> Promedio por estudiante >>>>>>>>>>>")
    for i in range(estudiantes):
        promedio = sum(calificaciones[i]) / materias
        print(f"Estudiante {i+1}: {promedio:.2f}")

    print("\n>>>>>>>>>>> Promedio por materia >>>>>>>>>>>>")
    for j in range(materias):
        suma = 0
        for i in range(estudiantes):
            suma += calificaciones[i][j]
        promedio = suma / estudiantes
        print(f"Materia {j+1}: {promedio:.2f}")

    total = [cal for fila in calificaciones for cal in fila]
    calificacion_alta = max(total)
    calificacion_baja = min(total)

    print("\n>>>>>>>>>> Calificaciones Generales >>>>>>>>>>")
    print(f"Calificación más alta: {calificacion_alta}")
    print(f"Calificación más baja: {calificacion_baja}")
    print("\n------------------------------------------\n")

escuelita_sistema()
