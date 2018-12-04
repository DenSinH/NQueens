# NQueens
A Python solution to the N Queens problem

A friend of mine told me about this problem, so I decided to find a solution for it myself. The unique solutions are solutions which cannot be obtained from another solution by rotation or reflection. This is one of the principles I used in my code: the first queen only needs to be placed on the bottom left octant of the board, and I needn't check for any solutions for a certain configuration of queens if I have already found a solution for a reflection/rotation of this configuration. When placing the queens, I do so from bottom to top, since in the end, all rows need to have exactly one queen in them. This means that the first queen only needs to be placed on the first half of the bottom row. The second queen is placed on the second row, etc.

The locations for the queens are stored in an array, where the index is the x-coordinate, and the value is the y-coordinate. This saves memory, and makes it so the queens are always ordered, and do not have to be sorted before being put in the dictionary.

| N  | unique | total | time (s)          | new time (s)     |
|----|--------|-------|-------------------|------------------|
| 1  | 1      | 1     | 0.0               | 0.0              |
| 2  | 0      | 0     | 0.000999927520752 | 0.0              |
| 3  | 0      | 0     | 0.00100016593933  | 0.0              |
| 4  | 1      | 2     | 0.00399994850159  | 0.00200009346008 |
| 5  | 2      | 10    | 0.00999999046326  | 0.00600004196167 |
| 6  | 1      | 4     | 0.0209999084473   | 0.00799989700317 |
| 7  | 6      | 40    | 0.0820000171661   | 0.0310001373291  |
| 8  | 12     | 92    | 0.272000074387    | 0.0859999656677  |
| 9  | 46     | 352   | 1.09299993515     | 0.409999847412   |
| 10 | 92     | 724   | 4.45200014114     | 1.19799995422    |
| 11 | 341    | 2680  | 22.5130000114     | 5.3180000782     |
| 12 | 1787   | 14200 | 112.617000103     | 24.6129999161    |
| 13 | 9233   | 73712 | N/A               | 148.566999912    |

It may not be the most efficient code, but I cannot find any more ways to improve it.

It turns out I could by using more symmetry arguments, and by basically changing the problem for N into the problem for N - 1. The new updated times are in the table
