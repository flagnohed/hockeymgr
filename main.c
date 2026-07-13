#include "player.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static const char help[] = "Usage: hockeymgr <options>\n"
                           "-h, --help\n"
                           "\tPrint this message.\n"
                           "-t, --test\n"
                           "\tRun all tests.\n";

static void test_random_player(void) {
    Player_t *random_player = create_random_player(POS_LD);
    print_player(random_player);
}

int main(int argc, char **argv) {
    if (argc == 2) {
        if (!strcmp(argv[1], "-h") || !strcmp(argv[1], "--help")) {
            printf("%s", help);
            return 0;
        }
        if (!strcmp(argv[1], "-t") || !strcmp(argv[1], "--help")) {
            /* Place all tests here. */
            test_random_player();
            return 0;
        }
    }
    srand(time(NULL));
    return 0;
}


