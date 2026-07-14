#include "player.h"
#include <stdio.h>

static char *pos_to_str(Position_t position) {
    switch (position) {
        case POS_GOALIE:
            return "Goalie";
        case POS_DEFENSEMAN:
            return "Defenseman";
        case POS_FORWARD:
            return "Forward";
        default:
            return "Unknown";
    }
}

void player_print(Player_t *player, bool skip_attrs) {
    printf("%s, %u\n", player->name, player->age);
    printf("Height:   %u cm\n", player->height);
    printf("Weight:   %u kg\n", player->weight);
    printf("Position: %s\n", pos_to_str(player->position));
    printf("Handed:   %s\n", (player->hand == 'L' ? "Left" : "Right"));
    if (skip_attrs) return;
    printf("Shooting: %u\n", player->attrs->shooting);
    printf("Skating:  %u\n", player->attrs->skating);
    printf("Passing:  %u\n", player->attrs->passing);
    printf("Hitting:  %u\n", player->attrs->hitting);
    printf("Defense:  %u\n", player->attrs->defense);
}
