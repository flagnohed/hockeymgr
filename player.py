from dataclasses import dataclass
import random


NATION_MAP = {"SWE": "Sweden"}
POSITION_MAP = {"G": "Goalie", "D": "Defender", "F": "Forward"}


@dataclass
class Player():    
    # Static attributes
    name: str = ""
    age: int = 0
    height: int = 0  # In centimeters
    weight: int = 0  # In kilos
    handed: str = ""  # 'L' or 'R'
    nation: str = "SWE"
    position: str = ""
    total: int = 0      # derived from Skater/Goalie attributes
    # Hidden attributes
    # @todo: figure out how to implement this
    development_factor = 0
    max_potential = 0


@dataclass
class Skater(Player):
    # Visible attributes
    shooting = 0
    passing = 0
    off_aware = 0
    speed = 0
    bodycheck = 0
    stickcheck = 0
    def_aware = 0
    shotblock = 0
    strength = 0


@dataclass
class Goalie(Player):
    # Visible attributes
    reflex = 0
    speed = 0
    positioning = 0
    glove = 0
    blocker = 0
    agility = 0  # Sv. "vighet"


def read_names_from_txt(fname: str) -> list[str]:
    names: list[str] = []
    with open(fname, "r", errors="replace") as f:
        names = f.readlines()
    for i in range(len(names)):
        names[i] = "".join([c for c in names[i] if c.isalpha()])
    return names


def generate_random_name(nation: str = "SWE") -> str:
    if nation not in NATION_MAP.keys():
        print(f"Invalid nation: {nation}")
        exit(1)

    firsts = read_names_from_txt(f"names/firstname_{nation}.txt")
    lasts = read_names_from_txt(f"names/lastname_{nation}.txt")

    return random.choice(firsts) + " " + random.choice(lasts)


def generate_random_handedness(pos: str) -> str:
    # 89 - 11% L-R goalies in NHL history
    # 62 - 38% L-R skaters (NHL jan 2018)
    w = [0.89, 0.11] if pos == "G" else [0.62, 0.38]
    return random.choices(["Left", "Right"], weights=w, k=1)[0]


def generate_random_age() -> int:
    return random.choice(range(18, 35))


def generate_random_measurements() -> tuple[int, int]:
    HEIGHT_MEAN: float = 185.0
    HEIGHT_SIGMA: float = 7.5  # 170-200 cm
    WEIGHT_SIGMA: float = 10.0
    height = int(random.normalvariate(HEIGHT_MEAN, HEIGHT_SIGMA))
    # Assume "normal hockey-weight" is e.g. 80kg at 180cm. 
    weight_mean = height - 100
    weight = int(random.normalvariate(weight_mean, WEIGHT_SIGMA))
    return height, weight


def random_attribute_value() -> int:
    mean = 70.0
    stdd = 10.0
    return int(random.normalvariate(mean, stdd))


def generate_random_attributes_goalie(g: Goalie) -> None:
    """ Generates random attributes for skaters. 
        Attributes generated in this function are those
        present in the Goalie dataclass. The attributes
        present in the parent Player dataclass are generated
        elsewhere. """
    NUM_ATTRS: int = 6
    g.reflex = random_attribute_value()
    g.speed = random_attribute_value()
    g.positioning = random_attribute_value()
    g.glove = random_attribute_value()
    g.blocker = random_attribute_value()
    g.agility = random_attribute_value()

    g.total = int((g.reflex + g.speed + g.positioning + \
               g.glove + g.blocker + g.agility) / NUM_ATTRS)
    

def generate_random_attributes_skater(s: Skater) -> None:
    """ Generates random attributes for skaters. 
        Attributes generated in this function are those
        present in the Skater dataclass. The attributes
        present in the parent Player dataclass are generated
        elsewhere. """
    NUM_ATTRS: int = 8
    # Offensive attributes
    s.shooting = random_attribute_value()
    s.passing = random_attribute_value()
    s.off_aware = random_attribute_value()
    s.speed = random_attribute_value()

    # Defensive attributes
    s.stickcheck = random_attribute_value()
    s.def_aware = random_attribute_value()
    s.shotblock = random_attribute_value()
    s.strength = random_attribute_value()

    s.total = int((s.shooting + s.passing + s.off_aware + s.speed + \
                   s.stickcheck + s.def_aware + s.shotblock + s.strength) / NUM_ATTRS)
     

def generate_random_player(pos: str = "",
                           nation: str = "SWE") -> Player:
    if not pos:
        pos = random.choice(list(POSITION_MAP.keys()))

    p = Goalie() if pos == "G" else Skater()
    p.name = generate_random_name(nation)
    p.handed = generate_random_handedness(pos)
    p.age = generate_random_age()
    p.height, p.weight = generate_random_measurements()
    p.position = pos
    p.nation = nation

    if p.position == "G":
        generate_random_attributes_goalie(p)
    else:
        generate_random_attributes_skater(p)

    return p


DELIMITER: str = 25 * "-"


def print_player_info(p: Player) -> None:
    print(DELIMITER)
    print(f"| [{p.nation}] {p.name}, {p.age}")
    print(f"| Position: {POSITION_MAP[p.position]}")
    prefix = "| Catches" if p.position == "G" else "| Shoots"
    print(prefix + f": {p.handed}")
    print(f"| Height: {p.height} cm")
    print(f"| Weight: {p.weight} kg")
    print(f"| Total:  {p.total} OVR")


def print_goalie_attributes(g: Goalie) -> None:
    print(DELIMITER)
    print(f"| Agility:     {g.agility}")
    print(f"| Blocker:     {g.blocker}")
    print(f"| Glove:       {g.glove}")
    print(f"| Positioning: {g.positioning}")
    print(f"| Reflexes:    {g.reflex}")
    print(f"| Speed:       {g.speed}")
    print(DELIMITER)


def print_skater_attributes(s: Skater) -> None:
    print(DELIMITER)
    print(f"| Offensive awareness: {s.off_aware}")
    print(f"| Passing:             {s.passing}")
    print(f"| Shooting:            {s.shooting}")
    print(f"| Speed:               {s.speed}")
    print(DELIMITER)
    print(f"| Defensive awareness: {s.def_aware}")
    print(f"| Stick checking:      {s.stickcheck}")
    print(f"| Shot blocking:       {s.shotblock}")
    print(f"| Strength:            {s.strength}")
    print(DELIMITER)


def print_player(p: Player) -> None:
    print_player_info(p)
    if p.position == "G":
        print_goalie_attributes(p)
    else:
        print_skater_attributes(p)