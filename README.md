# Game-of-Life-GUI
An implementation of John Horton Conway's Game of Life (1970) as a graphical user interface. The Game of Life is a Turing complete cellular automaton, with evolution determined entirely by its initial state. This implementation is written in Python, using the Pygame library.

<p align="center">
  <img src="https://github.com/talhaahussain/Game-of-Life-GUI/blob/main/game.gif" alt="A GIF demonstration of the Game of Life" width=600 height=600>
</p>

### Description

Game of Life is a cellular automaton that involves a universe of square cells, arranged in a grid. A cell can either be alive or dead, and interacts with 8 neighbours*, in all 8 directions. At each time step, each cell follows these rules:

- A live cell with less than 2 alive neighbours dies (starvation)
- A live cell with 2 or 3 alive neighbours remains alive
- A live cell with more than 3 alive neighbours dies (overpopulation)
- A dead cell with exactly 3 alive neighbours becomes live (reproduction)

**this implementation uses the Moore neighbourhood; future versions may support Moore or von Neumann neighbourhoods.*

Currently, this version of Game of Life only allows for random initial seeds; future versions will support user input to customise the initial state.

### Prerequisites

Prerequisites are viewable in `requirements.txt`.

### Installation

Clone with:

```shell
git clone https://github.com/talhaahussain/Game-of-Life-GUI.git gameoflife
cd gameoflife/
```

Install prerequisites with:

```shell
pip install -r requirements.txt
```

### Usage

Run with:

```shell
cd src/
python gameoflife.py
```

### See also

[find_neighbours.py](https://gist.github.com/talhaahussain/133fe1a05242858376341d9401f008bb)
