calificaciones = [8.5, 4.0, 9.2, 6.0, 7.5]
# A) Obtener la calificación del primer estudiante y la del último.
primer_estudiante = calificaciones[0]
ultimo_estudiante = calificaciones[-1]
print("Calificación del primer estudiante:", primer_estudiante)
print("Calificación del último estudiante:", ultimo_estudiante)
# B) Calcular la suma del primer y el último elemento.
suma_cal = primer_estudiante + ultimo_estudiante
print('Suma de las calificaciones de el primer estudiante y el ultimo', suma_cal)
# C) Calcular la nota media.
num_notas=len(calificaciones)
suma_notas=sum(calificaciones)
nota_media=suma_notas/num_notas
print("Nota media:", nota_media)