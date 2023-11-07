def print_error(message):
    print(message)


def file_reader(arguments):
    global CURRENT_FILENAME
    if not arguments:
        print_error("Veuillez spécifier un nom de fichier.")
        return
    filename = arguments[0]
    try:
        with open(filename, "r"):
            print(f"{filename} chargé avec succès !")
            CURRENT_FILENAME = filename
    except FileNotFoundError:
        print_error("Le fichier spécifié n'existe pas.")


def info(args):
    global CURRENT_FILENAME
    if not CURRENT_FILENAME:
        print_error("Pas de fichier ouvert")
        return
    with open(CURRENT_FILENAME, "r") as file:
        file_length = 0
        for line_count, line in enumerate(file):
            file_length += len(line)
        print(f"Le fichier {CURRENT_FILENAME} contient {line_count + 1} lignes pour {file_length} caractères.")


def words(args):
    global CURRENT_FILENAME
    global LIST_OF_WORDS
    if not CURRENT_FILENAME:
        print_error("Pas de fichier ouvert")
        return
    list_of_words = []
    with open(CURRENT_FILENAME, "r") as file:
        for line in file:
            list_of_words.append(line.split(",")[0])
    LIST_OF_WORDS = list_of_words
    print("La liste de mots est mise à jour selon le fichier ouvert !")


def search(args):
    global LIST_OF_WORDS
    if not LIST_OF_WORDS:
        print_error("Pas de liste de mots initialisée : essayez \"words\" après avoir chargé un fichier")
        return
    if not args:
        print_error("Veuillez spécifier un mot à chercher.")
        return
    if args[0] in LIST_OF_WORDS:
        print(f"Le mot {args[0]} est dans la liste du fichier {CURRENT_FILENAME}.")
    else:
        print(f"Le mot {args[0]} n'est pas dans la liste du fichier {CURRENT_FILENAME}.")


def sum_of_numbers(args):
    try:
        print(f"La somme des nombres fournis est : {sum(list(map(float, args)))}")
    except ValueError:
        print_error(
            "Les valeurs fournies ne sont pas toutes des nombres. Le séparateur décimal est le point (Ex : 5.9).")


def avg(args):
    try:
        print(f"La moyenne arithmétique des nombres fournis est : {sum(list(map(float, args))) / len(args)}")
    except ValueError:
        print_error(
            "Les valeurs fournies ne sont pas toutes des nombres. Le séparateur décimal est le point (Ex : 5.9).")


def helper(args):
    print("Commandes possibles : \n"
          "file <name>: spécifier le nom d'un fichier sur lequel travailler\n"
          "info: montrer le nombre de lignes et de caractères du fichier\n"
          "words: utiliser le fichier comme liste de mots\n"
          "search <word>: déterminer si le mot est dans la liste de mots\n"
          "sum <number1> ... <numbern>: calculer la somme des nombres spécifiés\n"
          "avg <number1> ... <numbern>: calculer la moyenne des nombres spécifiés\n"
          "help: liste des commandes possibles\n"
          "exit: arrêter l'assistant")


def exiter(args):
    global RUNNING
    RUNNING = False


def execute(user_input):
    command_line = user_input.split()
    try:
        command = command_line[0]
    except:
        print_error("Veuillez entrer une commande.")
        return
    if command not in COMMANDS:
        print_error("Cette commande n'est pas valide.")
        return
    COMMANDS[command](command_line[1:])


def assistant():
    global RUNNING
    print("Bienvenue dans votre assistant Pythonicus !")
    while RUNNING:
        user_input = input(" > ")
        execute(user_input)


# Variables globales
COMMANDS = {
    "file": file_reader,
    "info": info,
    "words": words,
    "search": search,
    "sum": sum_of_numbers,
    "avg": avg,
    "help": helper,
    "exit": exiter
}
LIST_OF_WORDS = []
CURRENT_FILENAME: str = ""
RUNNING = True
if __name__ == '__main__':
    assistant()
