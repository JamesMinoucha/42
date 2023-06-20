from rich import print
import os


##conv = 'conv [file] [to] %'
bannedFunctionCalls = ["clearTerminal"]

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')
clearTerminal()

getVaraible = 'getVar [!name]%'
def getVariable(name):
    return getattr(globals(), name)

clear = 'clear %'
def clear():
    clearTerminal()
    print("[green]Successfully clear.[/green]")

def commandPrompt():
    command = input('>> ')
    commandSplit = command.split()

    if len(command) =< 0:
        print("NOP")
    try: 
        if commandSplit[0] in bannedFunctionCalls:
            print(f"[red]Commande déjà utiliser par la shell.[/red]")
        else:
            print(f"[green]Commande valide.[/green]")
    except:
        print(f"[red]Commande invalide.[/red]")

while True:
    commandPrompt()
    print("")