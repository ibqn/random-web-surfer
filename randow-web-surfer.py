from pystdlib import (
    stdarray,
    stdio,
)

print("random web surfer")

n = stdio.readInt()

links_count = stdarray.create2D(n, n, 0)
out_degrees = stdarray.create1D(n, 0)

while not stdio.isEmpty():
    # Accumulate link counts.
    i = stdio.readInt()
    j = stdio.readInt()

    out_degrees[i] += 1
    links_count[i][j] += 1

stdio.writeln(f"{n}x{n} probability matrix")

for i in range(n):
    # Write probability distribution for row i.
    for j in range(n):
        # Write probability for column j.
        p = (0.9 * links_count[i][j] / out_degrees[i]) + (0.1 / n)
        stdio.writef("%6.2f", p)

    stdio.writeln()
