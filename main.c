#include "player.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static const char help[] = "Usage: hockeymgr <options>\n"
                           "-h, --help\n"
                           "\tPrint this message.\n";

static void test_print_player(void) {
    Player_t player;
    player.name = "Testo Testersson";
    player.position = POS_FORWARD;
    player.age = 26;
    player.hand = 'L';
    player.height = 195;
    player.weight = 100;

    Attributes_t attrs;
    player_set_random_attrs(&attrs);
    player.attrs = &attrs;
    player_print(&player, false);
}

int main(int argc, char **argv) {
    if (argc == 2) {
        if (!strcmp(argv[1], "-h") || !strcmp(argv[1], "--help")) {
            printf("%s", help);
            return 0;
        }
    }
    srand(time(NULL));
    test_print_player();
    return 0;
}


