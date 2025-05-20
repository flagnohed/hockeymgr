#include "player.h"

int main() {
    Player_t *random_player = create_random_player(POS_LD);
    print_player(random_player);
    return 0;
}


