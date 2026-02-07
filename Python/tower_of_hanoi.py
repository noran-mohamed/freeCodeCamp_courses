def hanoi_solver(disks):
    rod1 = [i for i in range(disks, 0, -1)]
    rod2 = []
    rod3 = []
    
    moves = []

    def record():
        moves.append(f"{rod1} {rod2} {rod3}")
    
    record()

    def move(n, src, tgt, aux):
        if n == 0:
            return
        
        move(n-1, src, aux, tgt)

        tgt.append(src.pop())
        record()

        move(n-1, aux, tgt, src)

    move(disks, rod1, rod3, rod2)
    return "\n".join(moves)

