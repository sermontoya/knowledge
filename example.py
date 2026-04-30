from logic import And, Not, Implication, Or, Biconditional, Symbol, model_check
# ejemplo base

# Symbols
# "Rain"
# "Hagrid"
# "Dumbledore"

rain = Symbol("Rain")
hagrid = Symbol("Hagrid")
dumbledore = Symbol("Dumbledore")

# knowledge
knowledge = And()
knowledge.add(Implication(Not(rain), hagrid))
knowledge.add(And(Or(hagrid, dumbledore), Not(And(hagrid, dumbledore))))
knowledge.add(dumbledore)
# (h v d) ^ ¬(h ^ d))


# Si no llovió, Harry visitó a Hagrid hoy
# Harry visitó a Hagrid o a Dumbledore hoy, pero no a ambos
# Harry visitó a Dumbledore hoy
print("====== EJEMPLO 0: HARRY POTTER ======")
print(f"Rain: {model_check(knowledge, rain)}")
print(f"Hagrid: {model_check(knowledge, hagrid)}")
print(f"Dumbledore: {model_check(knowledge, dumbledore)}")


"""
1. Si estudio o hago tareas, entonces paso el curso, pero si no estudio, no paso.
Dado que: estudio
¿paso el curso? → True
¿no paso el curso? → False

((E v T) -> C) ^ (¬E -> ¬C)
"""

estudiar = Symbol("Estudiar")
tareas = Symbol("Hacer tareas")
curso = Symbol("Aprobar el curso")

knowledge = And()
knowledge.add(Implication(Or(estudiar, tareas), curso))
knowledge.add(Implication(Not(estudiar), Not(curso)))
knowledge.add(estudiar)

print("====== EJEMPLO 1: PASAR EL CURSO ======")
print(f"Estudiar: {model_check(knowledge, estudiar)}")
print(f"Hacer tareas: {model_check(knowledge, tareas)}")
print(f"Paso el curso?: {model_check(knowledge, curso)}")

"""
2. Si estudio, entonces si hago tareas paso el curso.
(E -> (T -> C))
Dado que: estudio, hago tareas

¿paso el curso? → True

"""
knowledge = And()
knowledge.add(Implication(estudiar, Implication(tareas, curso)))
knowledge.add(estudiar)
knowledge.add(tareas)

print("====== EJEMPLO 2: PASAR EL CURSO V2 ======")
print(f"Estudiar: {model_check(knowledge, estudiar)}")
print(f"Hacer tareas: {model_check(knowledge, tareas)}")
print(f"Paso el curso?: {model_check(knowledge, curso)}")

"""
3. Voy al cine si y solo si termino la tarea y no estoy cansado.

Dado que: termino la tarea, no estoy cansado

- ¿voy al cine? → True
- ¿no voy al cine? → False

C <-> (T ^ ¬Cansado)
"""

cine = Symbol("Voy al cine")
tarea = Symbol("Termino la tarea")
cansado = Symbol("Estoy cansado")

knowledge = And()
knowledge.add(Biconditional(cansado, And(tarea, Not(cansado))))
knowledge.add(tarea)
knowledge.add(Not(cansado))
print("====== EJEMPLO 3: CINE ======")
print(f"Termino la tarea: {model_check(knowledge, tarea)}")
print(f"Estoy cansado: {model_check(knowledge, cansado)}")
print(f"Voy al cine?: {model_check(knowledge, cine)}")

"""
4. Si el sistema responde y no hay timeout, entonces la transacción se procesa; de lo contrario, falla.

Dado que: el sistema responde, no hay timeout

- ¿la transacción se procesa? → True
- ¿la transacción falla? → False

(S ^ ¬T) -> P
"""
sistema = Symbol("El sistema responde")
timeout = Symbol("Hay timeout")
procesar = Symbol("La transacción se procesa")

knowledge = And()
knowledge.add(Implication(And(sistema, Not(timeout)), procesar))
knowledge.add(sistema)
knowledge.add(Not(timeout))

print("====== EJEMPLO 4: TRANSACCION ======")
print(f"El sistema responde: {model_check(knowledge, sistema)}")
print(f"Hay timeout: {model_check(knowledge, timeout)}")
print(f"La transacción se procesa: {model_check(knowledge, procesar)}")


"""
5. No es cierto que si estudio entonces paso.

- ¿estudio? → True
- ¿no paso? → True

¬(E -> P)
"""

knowledge = And(Not(Implication(estudiar, curso)))

print("====== EJEMPLO 5: NEGACION ======")
print(f"Estudiar: {model_check(knowledge, estudiar)}")
print(f"Paso el curso?: {model_check(knowledge, curso)}")   



