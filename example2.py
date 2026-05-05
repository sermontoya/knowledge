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
