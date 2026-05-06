from logic import And, Not, Implication, Or, Biconditional, Symbol, model_check

"""
- To enter the server room, you need an employee card and a PIN code.
(C ^ P) -> S 
- To enter the meeting room, you need an employee card or to be a registered visitor.
(C v V) -> M
- If you are a registered visitor, then you cannot access the server room.
V -> ¬S
- If the system is in emergency mode, then all doors open without restriction.
E -> (S ^ M)
- If there is an intruder alert, then emergency mode is not activated.
A -> ¬E

- Ana has an employee card.
- Ana does not have a PIN code.
- The system is not in emergency mode.
"""
server = Symbol("Server Room")
meeting = Symbol("Meeting Room")
card = Symbol("Employee Card")
pin = Symbol("PIN Code")
visitor = Symbol("Registered Visitor")
emergency = Symbol("Emergency Mode")
alert = Symbol("Intruder Alert")

knowledge = And()
knowledge.add(Implication(And(card, pin), server))
knowledge.add(Implication(Or(card, visitor), meeting))
knowledge.add(Implication(visitor, Not(server)))
knowledge.add(Implication(emergency, And(server, meeting)))
knowledge.add(Implication(alert, Not(emergency)))

knowledge.add(card)
knowledge.add(Not(pin))
knowledge.add(Not(emergency))

print("====== Caso 1: Smart Building ======")
print(f"Ana puede entrar a Server Room?: {model_check(knowledge, server)}")
print(f"Ana puede entrar al Meeting Room?: {model_check(knowledge, meeting)}")

knowledge.add(alert)
print(f"\nSi la alerta se activa, Ana puede entrar al Server Room ahora?: {model_check(knowledge, server)}")

"""
There are three possible suspects:

- ColMustard
- ProfPlum
- MsScarlet

There are three possible rooms:

- ballroom
- kitchen
- library

There are three possible weapons:

- knife
- revolver
- wrench
"""
col = Symbol("ColMustard")
prof = Symbol("ProfPlum")
ms = Symbol("MsScarlet")

ball = Symbol("Ballroom")
kitchen = Symbol("Kitchen")
library = Symbol("Library")

knife = Symbol("Knife")
revolver = Symbol("Revolver")
wrench = Symbol("Wrench")

personajes = [col, prof, ms]
lugares = [ball, kitchen, library]
armas = [knife, revolver, wrench]
"""

- There must be at least one character involved.
- There must be at least one room involved.
- There must be at least one weapon involved.

"""
knowledge = And()
knowledge.add(Or(col, prof, ms))
knowledge.add(Or(ball, kitchen, library))
knowledge.add(Or(knife, revolver, wrench))

"""
- ColMustard is not involved.
 ¬Col
- The crime did not happen in the kitchen.
 ¬Kit
- The weapon was not the revolver.
 ¬revolver
 
- At least one of the following is false:
  - MsScarlet is involved.
  - The crime happened in the library.
  - The weapon was the wrench.
  
  (¬Ms v ¬L v ¬W)
- ProfPlum is not involved.
¬Prof
- The crime did not happen in the ballroom.
¬Ball
"""
knowledge.add(Not(col))
knowledge.add(Not(kitchen))
knowledge.add(Not(revolver))
knowledge.add(Or(Not(ms), Not(library), Not(wrench)))
knowledge.add(Not(prof))
knowledge.add(Not(ball))


print("====== Caso 2: Clue Mystery ======")
print(f"ColMustard fue el culpable?: {model_check(knowledge, col)}")
print(f"ProfPlum fue el culpable?: {model_check(knowledge, prof)}")
print(f"MsScarlet fue el culpable?: {model_check(knowledge, ms)}\n")

print(f"Ocurrió en el salón?: {model_check(knowledge, ball)}")
print(f"Ocurrió en la cocina?: {model_check(knowledge, kitchen)}")
print(f"Ocurrió en la librería?: {model_check(knowledge, library)}\n")

print(f"Fue con el cuchillo?: {model_check(knowledge, knife)}")
print(f"Fue con el revolver?: {model_check(knowledge, revolver)}")
print(f"Fue con la llave inglesa?: {model_check(knowledge, wrench)}")

def determinarCulpable(conocimiento, personajes):
    posibles_culpables = []
    for personaje in personajes:
        if model_check(conocimiento, personaje):
            posibles_culpables.append(personaje)
    if len(posibles_culpables) == 0:
        return "No se pudo determinar el culpable."
    elif len(posibles_culpables) == 1:
        return f"El culpable es {posibles_culpables[0]}"
    else:
        return f"Los culpables son {', '.join(str(personaje) for personaje in posibles_culpables)}"
def determinarLugar(conocimiento, lugares):
    posibles_lugares = []
    for lugar in lugares:
        if model_check(conocimiento, lugar):
            posibles_lugares.append(lugar)
    if len(posibles_lugares) == 0:
        return "No se pudo determinar el lugar del crimen."
    elif len(posibles_lugares) == 1:
        return f"El crimen ocurrió en {posibles_lugares[0]}"
    else:
        return f"Los lugares posibles son {', '.join(str(lugar) for lugar in posibles_lugares)}"

def determinarArmas(conocimiento, armas):
    posibles_armas = []
    for arma in armas:
        if model_check(conocimiento, arma):
            posibles_armas.append(arma)
    if len(posibles_armas) == 0:
        return "No se pudo determinar el arma."
    elif len(posibles_armas) == 1:
        return f"El arma utilizada fue {posibles_armas[0]}"
    else:
        return f"Las armas utilizadas son {', '.join(str(arma) for arma in posibles_armas)}"

print("\n") 
print(f"{determinarCulpable(knowledge, personajes)}")
print(f"{determinarLugar(knowledge, lugares)}")
print(f"{determinarArmas(knowledge, armas)}")


