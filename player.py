import random
import sys

NATION_MAP = {"SWE": "Sweden"}
POSITION_MAP = {"G": "Goalie", "D": "Defender", "F": "Forward"}


class Player:
    attr_mean = 70.0
    attr_stdd = 10.0
    height_mean: float = 185.0
    height_sigma: float = 7.5  # 170-200 cm
    weight_sigma: float = 10.0
    delimiter: str = 25 * "-"

    def __init__(self, _pos: str = ""):
        self.generate_random_player(_pos)
        # In the future, maybe read player from file here?

    def generate_random_player(self, pos):
        self.name = self.generate_random_name()
        self.age = self.generate_random_age()
        self.height, self.weight = self.generate_random_measurements()
        self.nation = "SWE"
        self.position = self.generate_random_position() if not pos else pos
        self.handed = self.generate_random_handedness()
        self.attrs = {}
        if self.position == "G":
            keys = [
                "reflexes",
                "speed",
                "positioning",
                "glove",
                "blocker",
                "agility",
            ]

        else:
            keys = [
                "shot",
                "speed",
                "passing",
                "off_aware",
                "def_aware",
                "bodycheck",
                "stickcheck",
                "strength",
            ]

        for k in keys:
            self.attrs[k] = self.generate_random_attribute_value()

        self.total = int(sum(self.attrs.values()) / len(self.attrs))

    def generate_random_position(self) -> str:
        return random.choice(list(POSITION_MAP.keys()))

    def read_names_from_txt(self, fname: str) -> list[str]:
        names: list[str] = []
        with open(fname, "r", errors="replace", encoding="utf-8") as f:
            names = f.readlines()
        for i in range(len(names)):
            names[i] = "".join([c for c in names[i] if c.isalpha()])
        return names

    def generate_random_name(self, nation: str = "SWE") -> str:
        if nation not in NATION_MAP:
            print(f"Invalid nation: {nation}")
            sys.exit(1)

        firsts = self.read_names_from_txt(f"names/firstname_{nation}.txt")
        lasts = self.read_names_from_txt(f"names/lastname_{nation}.txt")

        return random.choice(firsts) + " " + random.choice(lasts)

    def generate_random_handedness(self) -> str:
        # 89 - 11% L-R goalies in NHL history
        # 62 - 38% L-R skaters (NHL jan 2018)
        if not self.position:
            print("ERROR: Position needs to be set before handedness.")
            sys.exit(1)
        w = [0.89, 0.11] if self.position == "G" else [0.62, 0.38]
        return random.choices(["Left", "Right"], weights=w, k=1)[0]

    def generate_random_age(self) -> int:
        return random.choice(range(18, 35))

    def generate_random_measurements(self) -> tuple[int, int]:
        height = int(random.normalvariate(self.height_mean, self.height_sigma))
        # Assume "normal hockey-weight" is e.g. 80kg at 180cm.
        weight_mean = height - 100
        weight = int(random.normalvariate(weight_mean, self.weight_sigma))
        return height, weight

    def generate_random_attribute_value(self) -> int:
        return int(random.normalvariate(self.attr_mean, self.attr_stdd))

    def print_player_info(self) -> None:
        print(self.delimiter)
        print(f"| [{self.nation}] {self.name}, {self.age}")
        print(f"| Position: {POSITION_MAP[self.position]}")
        prefix = "| Catches" if self.position == "G" else "| Shoots"
        print(prefix + f": {self.handed}")
        print(f"| Height: {self.height} cm")
        print(f"| Weight: {self.weight} kg")
        print(f"| Total:  {self.total} OVR")

    def print(self):
        self.print_player_info()
        print(self.delimiter)
        for k, v in self.attrs.items():
            print(f"| {k}: {v}")
        print(self.delimiter)
