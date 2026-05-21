Change_hat(Hat.Purple_hat)
do_a_flip()
while True:
    if can_harvest():
        harvest()
        move(North)
    do_a_flip()