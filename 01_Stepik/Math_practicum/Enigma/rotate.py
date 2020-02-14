def rotate(shift_in, line_in):
    shift_cond = {1: [17], 2: [5], 3: [22], 4: [10], 5: [0], 6: [0, 13], 7: [0, 13], 8: [0, 13]}
    next_rot[0] = 1
    for k in range(n_rot):
        shift_in[k] = (shift_in[k] + next_rot[k]) % 26
    next_rot[1:] = [0, 0]

    for n in range(n_rot - 1):
        if shift_in[n] + 1 in shift_cond[line_in[n]]:
            next_rot[n] = 1
            next_rot[n + 1] = 1
            break
    return shift_in

n_rot = 3

shift = [3, 3, 3]
line = [2, 2, 2]
next_rot = [1, 0, 0]

for i in range(5):

    shift = rotate(shift, line)
