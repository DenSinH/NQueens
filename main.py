import numpy as np
import time


def mir(q):
    # mirroring in the diagonal
    q_ = -np.ones(q.size)
    n = q.size

    # only values for which the coordinate is greater than -1 are taken into account
    q_[q[q >= 0.].astype(int)] = np.arange(n)[q >= 0.]
    return q_


def r1(q):
    # rotating clockwise once
    q_ = -np.ones(q.size)
    n = q.size

    # only values for which the coordinate is greater than -1 are taken into account
    q_[q[q >= 0.].astype(int)] = n - 1 - np.arange(n)[q >= 0.]
    return q_


def r2(q):
    # rotating clockwise twice
    q_ = -np.ones(q.size)
    n = q.size

    # only values for which the coordinate is greater than -1 are taken into account
    q_[n - 1 - np.arange(n)[q >= 0.]] = n - 1 - q[q >= 0.]
    return q_


def rot_mir_queens(queens, n=8):
    # symmetries of the chess board

    for mirror in (mir, lambda q: q):
        for rot1 in (r1, lambda q: q):
            for rot2 in (r2, lambda q: q):

                yield mirror(rot1(rot2(queens)))


calculated_configs = {}


def place_queens(queens=None, board=None, n=8):
    # possible configurations we found
    # reporting progress only for the first call of the function
    possible_configs = []
    repxy = False

    if queens is None:
        # -1. is the placeholder coordinate
        queens = -np.ones(n)

    # generate the board if None was passed
    if board is None:

        # None is passed in the initial function call, we wish to keep track of progress, so repxy is true
        repxy = True
        board = np.ones((n, n))

        for x in np.nonzero(queens[queens >= 0])[0]:
            # horizontal and vertical paths
            board[x, :] = 0.
            board[:, queens[x]] = 0.

            # diagonal paths
            board[x + np.arange(max(-x, -queens[x]), n - max(x, queens[x])),
                  queens[x] + np.arange(max(-x, -queens[x]), n - max(x, queens[x]))] = 0.
            board[x + np.arange(max(-x, queens[x] - n + 1), min(n - 1 - x, queens[x])),
                  queens[x] - np.arange(max(-x, queens[x] - n + 1), min(n - 1 - x, queens[x]))] = 0.

    # if a board was passed, and we cannot place any queens on it, report the configuration
    elif np.all(board == np.zeros(board.shape)):
        return [queens]

    # building it up from the bottom
    # only checking x-coords where a queen can be placed
    y = queens[queens >= 0.].size
    nzx = np.nonzero(board[:, y])[0]

    # otherwise, loop over any unchecked spaces
    for x in nzx if not repxy else xrange(int(n/2. + 0.5)):
        # report if wanted
        if repxy:
            print x

        # place the new queen
        queens_ = np.array(queens)
        queens_[x] = y

        # check if we have already had (a symmetry) of this configuration
        # if so, the queens_ variable will be a key in results_for_queens
        for config in rot_mir_queens(queens_, n=n):
            if config.tostring() in calculated_configs:
                break
        else:

            # otherwise, create a new board, and find the possible configurations
            board_ = np.array(board)

            # horizontal and vertical paths
            board_[x, :] = 0.
            board_[:, y] = 0.

            # diagonal paths
            upward_diagonal = np.arange(max(-x, -y), n - max(x, y))
            downward_diagonal = np.arange(max(-x, y - n + 1), min(n - 1 - x, y))

            board_[x + upward_diagonal,
                   y + upward_diagonal] = 0.
            board_[x + downward_diagonal,
                   y - downward_diagonal] = 0.

            # amount of places a queen may be placed
            nonzero = board_[board_ == 1.].size

            # we only wish to find configurations with n queens, so if we cannot get n queens on the board, we can skip
            if nonzero + queens_[queens_ >= 0].size >= n:

                # otherwise, create a new recursion
                configs = place_queens(queens_, board=board_, n=n)
                possible_configs.extend(configs)

                # show that we have calculated for this configuration
                calculated_configs[queens_.tostring()] = 1.

    return possible_configs

if __name__ == "__main__":
  """Maximum length was N"""
  N = 8

  t0 = time.time()
  tot = []
  unique = 0

  for config in place_queens(n=N):
      unique += 1
      tot += set([str(config_) for config_ in rot_mir_queens(config, N)])

  comptime = time.time() - t0

  for q in tot:
      print q

  print len(tot), "total solutions"
  print unique, "unique solutions"
  print comptime, "seconds of computing time"