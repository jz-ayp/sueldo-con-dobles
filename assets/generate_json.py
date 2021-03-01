"""
Generar JSON para ejercicio de sueldo con horas dobles
"""

def sueldo_con_dobles(horas, tarifa):
    """Calcular sueldo tomando en cuenta horas extras dobles.
    Desglosa horas extras y sueldo por horas extras."""

    if horas <= 48:
        # Solo sencillas
        horas2 = 0
    else:
        horas2 = horas - 48
    sueldo2 = horas2 * tarifa * 2
    sueldoT = (horas - horas2) * tarifa + sueldo2
    return (sueldoT, horas2, sueldo2)


import json

FILENAME = ".github/classroom/autograding.json"

cases = [(47, 100), (48, 100), (49, 100), (51, 100), (48.5, 100)]

output = {}
tests = []

for horas, tarifa in cases:
    inp = f"{horas}\r\n{tarifa}"
    sueldoT, horas2, sueldo2 = sueldo_con_dobles(horas, tarifa)
    outp = "(\n|.)*".join(str(i) for i in (horas2, sueldo2, sueldoT))
    #outp = f"{total}(\n|.)*{comision}"
    name = f"Test{horas}"
    entry = {
        "name": name,
        "setup": "",
        "run": "LANG=en_US.utf8 timeout 3m python3 main.py",
        "input": inp,
        "output": outp,
        "comparison": "regex",
        "timeout": 1,
        "points": 1
        }
    tests.append(entry)
tests = {"tests": tests}

with open(FILENAME, "w") as f:
    json.dump(tests, f, indent=2)
