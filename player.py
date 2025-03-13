from enum import Enum
import random


NATIONS = ["SWE"]
POSITIONS = ["G", "D", "F"]

PLAYER_HEIGHT_MEAN = 185
PLAYER_HEIGHT_SIGMA = 7.5  # 170-200 cm
PLAYER_WEIGHT_MEAN = 90
PLAYER_WEIGHT_SIGMA = 10  # 70-110 kg


class Player():
    # Create an empty player (both skaters and goalies)
    def __init__(self):
        # Static attributes
        self.name: str = ""
        self.age: int = 0
        self.height: int = 0  # In centimeters
        self.weight: int = 0  # In kilos
        self.handed: str = ""  # 'L' or 'R'
        self.nation: str = "SWE"
        self.position: str = ""

        # Hidden attributes
        # @todo: figure out how to implement this
        self.development_factor = 0
        self.max_potential = 0


class Skater(Player):
    def __init__(self):
        super(Skater, self).__init__()
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
        super(Goalie, self).__init__()
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

    firsts = read_names_from_txt(f"names/firstname_{nation}.txt")
    lasts = read_names_from_txt(f"names/lastname_{nation}.txt")

    return random.choice(firsts) + " " + random.choice(lasts)


def generate_random_handedness(pos: str) -> str:
    # 89 - 11% L-R goalies in NHL history
    # 62 - 38% L-R skaters (NHL jan 2018)
    return random.choices(["L", "R"], 
                          weights=[0.89, 0.11] if pos == "G" else [0.62, 0.38], 
                          k=1)[0]


def generate_random_age() -> int:
    return random.choice(range(18, 35))


def generate_random_measurements() -> tuple[int, int]:
    """ Returns (HEIGHT, WEIGHT). 
        @todo: fix abnormal combos, like 173cm + 113kg """
    height = int(random.normalvariate(PLAYER_HEIGHT_MEAN, 
                                      PLAYER_HEIGHT_SIGMA))
    weight = int(random.normalvariate(PLAYER_WEIGHT_MEAN, 
                                      PLAYER_WEIGHT_SIGMA))
    return height, weight


def generate_random_player(pos: str = "",
                           nation: str = "SWE") -> Player:
    if not pos:
        pos = random.choice(POSITIONS)
    p = Goalie() if pos == "G" else Skater()
    p.name = generate_random_name(nation)
    p.handed = generate_random_handedness(pos)
    p.age = generate_random_age()
    p.height, p.weight = generate_random_measurements()
    p.position = pos
    p.nation = nation
    return p


def print_player(p: Player) -> None:
    print(f"[{p.nation}] {p.name}, {p.age}")
    print(f"Position: {p.position}")
    print(f"Height: {p.height} cm")
    print(f"Weight: {p.weight} kg")
    prefix = "Catches" if p.position == "G" else "Shoots"
    print(prefix + f": {p.handed}")
    