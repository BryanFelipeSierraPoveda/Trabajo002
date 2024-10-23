class Estudiante:
    def _init_(self, tipo_documento, numero_documento, nombres):
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.nombres = nombres
    
    def mostrar_informacion(self):
        print(f"Tipo de Documento: {self.tipo_documento}")
        print(f"Número de Documento: {self.numero_documento}")
        print(f"Nombres del Estudiante: {self.nombres}")


class Curso:
    def _init_(self, codigo_curso, nombre_curso):
        self.codigo_curso = codigo_curso
        self.nombre_curso = nombre_curso
    
    def mostrar_informacion(self):
        print(f"Código del curso: {self.codigo_curso}")
        print(f"Nombre del curso: {self.nombre_curso}")


class SesionCurso:
    def _init_(self, codigo_curso, hora_inicio, hora_final, fecha):
        self.codigo_curso = codigo_curso
        self.hora_inicio = hora_inicio
        self.hora_final = hora_final
        self.fecha = fecha
    
    def mostrar_informacion(self):
        print(f"Código del Curso: {self.codigo_curso}")
        print(f"Hora de Inicio: {self.hora_inicio}")
        print(f"Hora Final: {self.hora_final}")
        print(f"Fecha: {self.fecha}")


class Asistencia:
    def _init_(self, codigo_sesion, documento_estudiante, estado_asistencia, fecha_sesion):
        self.codigo_sesion = codigo_sesion
        self.documento_estudiante = documento_estudiante
        self.estado_asistencia = estado_asistencia
        self.fecha_sesion = fecha_sesion  # Agregamos el atributo para la fecha de la sesión
    
    def mostrar_informacion(self):
        print(f"Código de la Sesión: {self.codigo_sesion}")
        print(f"Documento del Estudiante: {self.documento_estudiante}")
        if self.estado_asistencia == 0:
            print("El estudiante llegó a tiempo.")
        elif self.estado_asistencia == 1:
            print("El estudiante llegó tarde.")
        elif self.estado_asistencia == 2:
            print("El estudiante no asistió.")


def buscar_estudiante_por_documento():
    numero_documento = input("Ingresa el número de documento del estudiante que deseas buscar: ")
    
    for i in range(len(estudiantes)):
        if estudiantes[i].numero_documento == numero_documento:
            estudiantes[i].mostrar_informacion()
            break
    else:
        print("No se encontró un estudiante con ese número de documento.")


estudiantes = []
cursos = []
sesiones = []
asistencias = []

def mostrar_menu():
    print("\n¡Hola! Este programa te ayudará a gestionar la información.")
    print("Elige una de las siguientes opciones:")
    print("1. Agregar un estudiante")
    print("2. Ingresar datos de un curso")
    print("3. Ingresar datos de una sesión")
    print("4. Ingresar datos de asistencia")
    print("5. Buscar estudiante por número de documento") 
    print("6. Listar datos de cursos")
    print("7. Listar datos de sesiones")
    print("8. Listar datos de asistencias")
    print("9. Mostrar estudiantes que llegaron tarde en una sesión específica")
    print("10. Mostrar cuántas veces un estudiante ha llegado tarde en un curso por rango de fechas")
    print("11. Salir del programa")


def estudiantes_tarde_sesion(fecha, hora_inicio, hora_final, codigo_curso):
    print(f"\nEstudiantes que llegaron tarde en la sesión del curso {codigo_curso} el {fecha} de {hora_inicio} a {hora_final}:")

    for sesion in sesiones:
        if (sesion.codigo_curso == codigo_curso and sesion.fecha == fecha and 
            sesion.hora_inicio == hora_inicio and sesion.hora_final == hora_final):
            
            for asistencia in asistencias:
                if asistencia.codigo_sesion == sesion.codigo_curso and asistencia.estado_asistencia == 1:
                    
                    for estudiante in estudiantes:
                        if estudiante.numero_documento == asistencia.documento_estudiante:
                            estudiante.mostrar_informacion()
                            print("Este estudiante llegó tarde.\n")
                            break
            break
    else:
        print("No se encontró ninguna sesión o estudiantes que hayan llegado tarde.")


def contar_tardanzas_por_curso(codigo_curso, fecha_inicio, fecha_fin, documento_estudiante):
    contador_tardanzas = 0
    
    for sesion in sesiones:
        if sesion.codigo_curso == codigo_curso and fecha_inicio <= sesion.fecha <= fecha_fin:
            for asistencia in asistencias:
                if (asistencia.codigo_sesion == sesion.codigo_curso and
                    asistencia.documento_estudiante == documento_estudiante and
                    asistencia.estado_asistencia == 1):
                    contador_tardanzas += 1
    
    return contador_tardanzas


while True:
    mostrar_menu()
    opcion = int(input("\n¿Qué opción vas a elegir? "))

    if opcion == 1:
        tipo_documento = input("Ingresa el tipo de documento: ")
        numero_documento = input("Ingresa el número de documento: ")
        nombres = input("Ingresa los nombres del estudiante: ")
        
        estudiante = Estudiante(tipo_documento, numero_documento, nombres)
        estudiantes.append(estudiante)
        
        print("Datos del estudiante guardados correctamente.")
        
    elif opcion == 2:
        codigo_curso = input("Ingresa el código del curso: ")
        nombre_curso = input("Ingresa el nombre del curso: ")
        
        curso = Curso(codigo_curso, nombre_curso)
        cursos.append(curso)
        
        print("Datos del curso guardados correctamente.")
        
    elif opcion == 3:
        codigo_curso = input("Ingresa el código del curso: ")
        hora_inicio = input("Ingresa la hora de inicio (formato HH:MM): ")
        hora_final = input("Ingresa la hora final (formato HH:MM): ")
        fecha = input("Ingresa la fecha (formato DD/MM/AAAA): ")

        sesion = SesionCurso(codigo_curso, hora_inicio, hora_final, fecha)
        sesiones.append(sesion)

        print("Datos de la sesión del curso guardados correctamente.")

    elif opcion == 4:
        codigo_sesion = input("Ingresa el código de la sesión: ")
        documento_estudiante = input("Ingresa el número de documento del estudiante: ")

        while True:
            estado = input("Ingrese el estado de asistencia:\n0 - Llegó a tiempo\n1 - Llegó tarde\n2 - No llegó\nOpción: ")
        
            if estado in ('0', '1', '2'):
                estado_asistencia = int(estado) 
                break
            else:
                print("Opción no válida. Por favor, elige 0, 1 o 2.")

        asistencia = Asistencia(codigo_sesion, documento_estudiante, estado_asistencia, fecha)
        asistencias.append(asistencia)

        print("Datos de la asistencia guardados correctamente.")  

    elif opcion == 5:
        buscar_estudiante_por_documento()

    elif opcion == 6:
        print("Datos de los cursos:")
        for curso in cursos:
            curso.mostrar_informacion()

    elif opcion == 7:
        print("Datos de las sesiones:")
        for sesion in sesiones:
            sesion.mostrar_informacion()

    elif opcion == 8:
        print("Datos de las asistencias:")
        for asistencia in asistencias:
            asistencia.mostrar_informacion()

    elif opcion == 9:
        fecha = input("Ingresa la fecha de la sesión (DD/MM/AAAA): ")
        hora_inicio = input("Ingresa la hora de inicio (formato HH:MM): ")
        hora_final = input("Ingresa la hora final (formato HH:MM): ")
        codigo_curso = input("Ingresa el código del curso: ")
        estudiantes_tarde_sesion(fecha, hora_inicio, hora_final, codigo_curso)

    elif opcion == 10:
        documento_estudiante = input("Ingresa el número de documento del estudiante: ")
        codigo_curso = input("Ingresa el código del curso: ")

        fecha_inicio = input("Ingresa la fecha de inicio (formato DD/MM/AAAA): ")
        fecha_fin = input("Ingresa la fecha de fin (formato DD/MM/AAAA): ")

        llegadas_tarde = 0

        for sesion in sesiones:
            if sesion.codigo_curso == codigo_curso:
             if fecha_inicio <= sesion.fecha <= fecha_fin:
                    for asistencia in asistencias:
                        if (asistencia.codigo_sesion == sesion.codigo_curso and
                            asistencia.documento_estudiante == documento_estudiante and
                            asistencia.estado_asistencia == 1): 
                            llegadas_tarde += 1

        print(f"\nEl estudiante con documento {documento_estudiante} llegó tarde {llegadas_tarde} veces en el curso {codigo_curso} entre {fecha_inicio} y {fecha_fin}.")