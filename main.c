#include "player.h"
#include <stdlib.h>
#include <time.h>

int main(void) {
    srand(time(NULL));
    Player_t *random_player = create_random_player(POS_LD);
    print_player(random_player);
    return 0;
}


