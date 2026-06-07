from logic import And, Not, Implication, Or, Biconditional, Symbol, model_check

fever = Symbol("Fever")
cough = Symbol("Cough")
flu = Symbol("Flu")
rash = Symbol("Rash")
measles = Symbol("Measles")
antiviral = Symbol("Antiviral Medication")
isolation = Symbol("Isolation")
test = Symbol("Blood test")
notify = Symbol("Notify public health authorities")



"""
- If there is fever and cough, then possible flu.
(F ^ C) -> Fl
- If there is fever and rash, then possible measles.
(F ^ R) -> M
- If there is flu, then prescribe antiviral medication.
Fl -> anti
- If there is measles, then prescribe isolation.
M -> I
- If there is fever but no cough and no rash, then order a blood test.
F ^ ¬C ^ ¬R
- If isolation is prescribed, then notify public health authorities.
I -> N
"""

knowledge = And()
knowledge.add(Implication(And(fever, cough), flu))
knowledge.add(Implication(And(fever, rash), measles))
knowledge.add(Implication(flu, antiviral))
knowledge.add(Implication(measles, isolation))
knowledge.add(And(fever, Not(cough), Not(rash)))
knowledge.add(Implication(isolation, notify))

"""
- The patient has fever.
- The patient has rash.
- The patient does not have cough.
"""
knowledge.add(fever)
knowledge.add(rash)
knowledge.add(Not(cough))


print("Diagnostics: \n")
if model_check(knowledge, flu):
    print("Flu is a possible diagnosis.")
if model_check(knowledge, measles):
    print("Measles is a possible diagnosis.")
if model_check(knowledge, isolation):
    print("Isolation is a possible diagnosis.")
if model_check(knowledge, notify):
    print("Notify public health authorities.")
