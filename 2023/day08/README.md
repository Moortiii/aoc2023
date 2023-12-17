Given that we reach Z after 1, 2, 3 and 5 steps for each path respectively. The minimum amount of steps taken is given by A * B * C * D (1 * 2 * 3 * 5 = 15).

- 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
D X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X
C . X . X . X . X . X . X . X . X . X . X . X . X . X . X . X
B . . X . . X . . X . . X . . X . . X . . X . . X . . X . . X
A . . . . X . . . . X . . . . X . . . . X . . . . X . . . . X

Pseudocode:

# A list of known step-intervals for a given path
paths = defaultdict(list)

Filter out paths that don't start with A.

For each of the paths:
    next_location = follow_path(current_position, instruction)

    if next_location.last_character == "Z":
        for step_interval in paths[path]:
            if current_steps % step_interval == 0:
                break
        else:
            paths[path].append(current_steps)

    if all paths have a valid step interval:
        return the multiplication of all the step intervals
        
        

