class Bg:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def warn(text):
    print(Bg.RED + Bg.UNDERLINE +Bg.BOLD + text + Bg.END)
def ok_green(text):
    print(Bg.GREEN + Bg.UNDERLINE +Bg.BOLD + text + Bg.END)
def ok_blue(text):
    print(Bg.BLUE + Bg.UNDERLINE +Bg.BOLD + text + Bg.END)

# print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

if __name__ == '__main__':
    warn("Felipe Gusmao")
    ok_blue("Felipe Gusmao")
    ok_green("Felipe Gusmao")

