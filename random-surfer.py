import random
from pystdlib import (
    stdio,
    stdarray,
)
from argparse import ArgumentParser

parser = ArgumentParser(description="Simulating a random surfer")
parser.add_argument(
    "moves",
    type=int,
    nargs="?",
    default=10000,
    help="number of simulation moves. default: 10000",
)
args = parser.parse_args()

moves = args.moves

# Ignore a string line.
stdio.readLine()

# Read size of the transition matrix.
n = stdio.readInt()

# p = [stdio.readFloat() for i in range(n) for j in range(n)]
p = stdarray.create2D(n, n, 0)
for i in range(n):
    for j in range(n):
        p[i][j] = stdio.readFloat()

hits = stdarray.create1D(n, 0)

# Start at page 0.
page = 0

for i in range(moves):
    r = random.random()
    total = 0.0
    for j in range(n):
        total += p[page][j]
        if r < total:
            page = j
            break

    hits[page] += 1

for v in hits:
    stdio.writef(f"{v / moves:8.5f}")
stdio.writeln()
