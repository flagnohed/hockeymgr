from player import Player


class Team:
    num_lines: int = 1
    def_per_line: int = 2
    fwd_per_line: int = 3
    
    def __init__(self, name: str):
        self.generate_random_team(name)

    def generate_random_team(self, name: str) -> None:
        """Fill team with 1 goalie, 2 defenders and 3 forwards."""
        self.name = name
        self.lines: list[list[Player]] = []
        self.goalie = Player("G")

        for _ in range(self.num_lines):
            line = []
            for _ in range(self.def_per_line):
                p = Player("D")
                line += [p]

            for _ in range(self.fwd_per_line):
                p = Player("F")
                line += [p]

            self.lines += [line]


    def save_to_file(self): ...

    def print_line(self, line_number: int = 1) -> None:
        player_divider = " - "
        line: list[Player] = self.lines[line_number - 1]
        fwd_names: str = ""
        def_names: str = ""
        for player in line:
            if player.position == "F":
                fwd_names += player.get_last_name() + player_divider
            elif player.position == "D":
                def_names += player.get_last_name() + player_divider
            else:
                print(f"Unknown player position: {player.position}")
        
        # Remove trailing " - "
        fwd_names = fwd_names[: -len(player_divider)]
        def_names = def_names[: -len(player_divider)]

        print(fwd_names)
        print(def_names)
        print(self.goalie.get_last_name())
