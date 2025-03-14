#!/usr/bin/env python3

from player import (
    Player,
    generate_random_player,
    print_player,
)


def main():
    test_player: Player = generate_random_player()
    print_player(test_player)


if __name__ == "__main__":
    main()
