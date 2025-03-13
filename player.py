from enum import Enum
import random


NATIONS = ["SWE"]


class Position(Enum):
    ERR = 0
    G = 1
    D = 2
    F = 3


class Player():
    # Create an empty player (both skaters and goalies)
    def __init__(self):
        # Static attributes
        self.name: str = ""
        self.height: int = 0  # In centimeters
        self.weight: int = 0  # In kilos
        self.handed: str = ""  # 'L' or 'R'
        self.nation: str = "SWE"
        self.position: Position = None

        # Hidden attributes
        self.development_factor = 0
        self.max_potential = 0


class Skater(Player):
    def __init__(self):
        super().__init__(self)
        # Visible attributes
        self.shot_pwr = 0
        self.shot_acc = 0
        self.passing = 0
        self.off_aware = 0
        self.speed = 0
        self.bodycheck = 0
        self.stickcheck = 0
        self.def_aware = 0
        self.shotblock = 0
        self.strength = 0


class Goalie(Player):
    def __init__(self):
        # Visible attributes
        super().__init__(self)
        self.reflex = 0
        self.speed = 0
        self.positioning = 0
        self.glove = 0
        self.blocker = 0
        self.agility = 0  # Sv. "vighet"


def read_names_from_txt(fname: str) -> list[str]:
    names: list[str] = []
    with open(fname, "r", errors="replace") as f:
        names = f.readlines()
    for i in range(len(names)):
        names[i] = "".join([c for c in names[i] if c.isalpha()])
    return names


def generate_random_name(nation: str = "SWE") -> str:
    if nation not in NATIONS:
        print(f"Invalid nation: {nation}")
        exit(1)

    firsts = read_names_from_txt(f"firstname_{nation}.txt")
    lasts = read_names_from_txt(f"lastname_{nation}.txt")

    return random.choice(firsts) + " " + random.choice(lasts)


def generate_random_handedness(pos: Position) -> str:
    # 89 - 11% L-R goalies in NHL history
    # 62 - 38% L-R skaters (NHL jan 2018)
    if pos == Position.G:
        return random.choices(["L", "R"],
                              weights=[0.89, 0.11], k=1)[0]

    return random.choices(["L", "R"],
                          weights=[0.62, 0.38], k=1)[0]


def generate_random_player(pos: Position = None,
                           nation: str = "SWE") -> Player:
    if not pos:
        pos = random.choice(e.value for e in Position)

    p = Goalie() if pos == Position.G else Skater()
    p.name = generate_random_name(nation)
    p.position = pos
    p.nation = nation
    p.handed = generate_random_handedness(pos)

