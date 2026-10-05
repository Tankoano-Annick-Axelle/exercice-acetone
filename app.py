import math
import matplotlib.pyplot as plt

# ============================================================
# DONNEES DU PROBLEME
# ============================================================

# Débit massique total d'acétone
debit_total = 38          # kg/h

# Température initiale
T_initiale = 10           # °C

# Pression initiale
P_initiale = 1            # atm

# Pourcentage du premier flux
pourcentage_flux1 = 0.40

# Pourcentage du deuxième flux
pourcentage_flux2 = 0.60


# ============================================================
# 1. CALCUL DES DEBITS DES DEUX FLUX
# ============================================================

debit_flux1 = debit_total * pourcentage_flux1
debit_flux2 = debit_total * pourcentage_flux2

print("========== DEBITS ==========")
print(f"Débit total       : {debit_total:.2f} kg/h")
print(f"Débit flux 1 (40%) : {debit_flux1:.2f} kg/h")
print(f"Débit flux 2 (60%) : {debit_flux2:.2f} kg/h")


# ============================================================
# 2. TEMPERATURE D'EBULLITION DE L'ACETONE
# ============================================================

# Equation d'Antoine :
#
# log10(P) = A - B / (T + C)
#
# P : pression en mmHg
# T : température en °C
#
# Constantes utilisées pour l'acétone
A = 7.02447
B = 1161.0
C = 224.0

# Conversion de la pression de atm en mmHg
P_mmHg = P_initiale * 760

# Résolution de l'équation d'Antoine :
T_eb = B / (A - math.log10(P_mmHg)) - C

print("\n========== TEMPERATURE D'EBULLITION ==========")
print(f"Pression : {P_initiale:.2f} atm")
print(f"Pression : {P_mmHg:.2f} mmHg")
print(f"Température d'ébullition de l'acétone : {T_eb:.2f} °C")


# ============================================================
# 3. ENERGIE NECESSAIRE POUR TRANSFORMER LE FLUX 2 EN VAPEUR
# ============================================================

# Propriétés physiques de l'acétone
Cp_liquide = 2.15       # kJ/(kg.K)
chaleur_latente = 518   # kJ/kg

# Masse du flux chauffé pendant 1 heure
m = debit_flux2         # kg/h

# ------------------------------------------------------------
# Etape 1 : énergie pour chauffer l'acétone de 10°C
# jusqu'à sa température d'ébullition
# ------------------------------------------------------------

Q_chauffage = m * Cp_liquide * (T_eb - T_initiale)

# ------------------------------------------------------------
# Etape 2 : énergie nécessaire pour vaporiser l'acétone
# ------------------------------------------------------------

Q_vaporisation = m * chaleur_latente

# ------------------------------------------------------------
# Energie totale
# ------------------------------------------------------------

Q_total = Q_chauffage + Q_vaporisation

print("\n========== BILAN ENERGETIQUE ==========")

print(f"Masse chauffée : {m:.2f} kg/h")
print(f"Cp liquide     : {Cp_liquide:.2f} kJ/(kg.K)")
print(f"Chaleur latente: {chaleur_latente:.2f} kJ/kg")

print(f"\nEnergie de chauffage : {Q_chauffage:.2f} kJ/h")
print(f"Energie de vaporisation : {Q_vaporisation:.2f} kJ/h")
print(f"Energie totale : {Q_total:.2f} kJ/h")

# Conversion en kW
Q_total_kW = Q_total / 3600

print(f"Energie totale : {Q_total_kW:.2f} kW")


# ============================================================
# 4. COURBE TEMPERATURE D'EBULLITION = f(PRESSION)
# ============================================================

# 25 points entre 0,1 atm et 3 atm
nombre_points = 25

pressions = []

for i in range(nombre_points):
    P = 0.1 + i * (3.0 - 0.1) / (nombre_points - 1)
    pressions.append(P)


# Calcul des températures d'ébullition
temperatures_eb = []

for P in pressions:

    # Conversion atm -> mmHg
    P_mmHg = P * 760

    # Equation d'Antoine
    T = B / (A - math.log10(P_mmHg)) - C

    temperatures_eb.append(T)


# ============================================================
# 5. AFFICHAGE DES 25 POINTS
# ============================================================

print("\n========== TEMPERATURE D'EBULLITION ==========")

for i in range(nombre_points):
    print(
        f"Point {i+1:2d} : "
        f"P = {pressions[i]:.3f} atm  -->  "
        f"Téb = {temperatures_eb[i]:.2f} °C"
    )


# ============================================================
# 6. TRACE DE LA COURBE
# ============================================================

plt.figure(figsize=(9, 6))

plt.plot(
    pressions,
    temperatures_eb,
    marker='o',
    linewidth=2
)

plt.xlabel("Pression (atm)")
plt.ylabel("Température d'ébullition (°C)")

plt.title(
    "Variation de la température d'ébullition de l'acétone\n"
    "en fonction de la pression"
)

plt.grid(True)

plt.tight_layout()

plt.show()