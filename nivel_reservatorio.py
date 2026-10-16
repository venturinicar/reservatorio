import random
from colorama import Fore, Style

niveis = [ "Nivel 1", "Nivel 2", "Nivel 3", "Nivel 4", "Nivel 5"]


nivel = random.choice(niveis)
print("\nNivel atual do reservatório:")
print("O reservaorio está no:", nivel)

def situacao_nivel(situacao): 
    
    if situacao == "Nivel 1": 
        return "Muito baixo (critico)" 
    elif situacao == "Nivel 2": 
        return "Nivel baixo" 
    elif situacao == "Nivel 3": 
        return "Nivel medio"
    elif situacao == "Nivel 4":
        return "Nivel alto" 
    else: 
        return "Muito alto (alerta)" 


if nivel == "Nivel 1":
    print(Fore.RED + situacao_nivel(nivel))
elif nivel == "Nivel 2":
    print(Fore.YELLOW + situacao_nivel(nivel))
elif nivel == "Nivel 3":
    print(Fore.GREEN + situacao_nivel(nivel))
elif nivel == "Nivel 4":
    print(Fore.CYAN + situacao_nivel(nivel))
else:
    print(Fore.BLUE + situacao_nivel(nivel))

print(Style.RESET_ALL)
