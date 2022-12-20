for i in range(len(A)/2,1)#!/:usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
import string
import re

host = "misc.chal.csaw.io"
port = 9000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
time.sleep(0.5)
ret = s.recv(8096).decode("utf-8")
print(ret)
found = re.findall(r"\d+", ret)
mi, mj = int(found[2]), int(found[3])
M = []
n = 64
SOLUCE = []
def reset():
    global M
    global n
    M[:] = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(".")
        M.append(row)

def grid():
    global M
    for row in M:
        for col in row:
            print(col, end='')
        print()

def mark(i, j):
    global M
    M[i][j] = "X"

def add(l):
    global M
    global SOLUCE
    SOLUCE.append(l)
    for i,j in l:
        if M[i][j] != ".":
            raise Exception(f"case alredy used in {i} {j}")
        M[i][j] = "*"
def add_list(l):
    for e in l:
        add(e)




def block_6(i, j):
    return (
        (i,j),
        (i+1, j),
        (i, j+1)
    ),( (i+1,j+1),
        (i+2,j),
        (i+2, j+1)
    )

def block_h_6(i,j):
    return (
        [(i,j), (i+1,j), (i,j+1) ],
        [(i+1, j+1), (i+1, j+2), (i, j+2)]
    )

def block_4_3(i,j):
    a,b = block_h_6(i,j)
    c,d = block_h_6(i+2, j)
    return [a,b,c,d]
def row_block_6(i):
    Ls = []
    for j in range(0,64,2):
        l1,l2 = block_6(i, j)
        Ls.append(l1)
        Ls.append(l2)
    return Ls

def fill_all_rows(i_mark):
    x = i_mark - (i_mark%3)
    i = 0
    for i in range(0, x, 3):
        l = row_block_6(i)
        add_list(l)
    i += 7
    for i in range(i, 64, 3):
        l = row_block_6(i)
        add_list(l)

def fill_all_cols(i_mark, j_mark):
    x = j_mark - (j_mark%3)
    i = i_mark - (i_mark%3)
    j = 0   
    for j in range(0, x, 3):
        l = block_4_3(i, j)
        add_list(l)
    j += 7
    for j in range(j, 64, 3):
        l = block_4_3(i, j)
        add_list(l)
#flag{m@n_that_was_sup3r_hard_i_sh0uld_have_just_taken_the_L}
def brute_force_16(i, j):
    l = [
        [(i+1,j), (i+1,j+1), (i,j+1)],
        [(i,j+2), (i,j+3), (i+1,j+3)],
        [(i+1,j+2),(i+2,j+1), (i+2,j+2) ],
        [(i+2,j),(i+3,j), (i+3,j+1) ],
        [(i+2,j+3),(i+3,j+2), (i+3,j+3) ],
    ]
    add_list(l)

def send_soluce():
    global SOLUCE
    global s
    t = []
    for a,b,c in SOLUCE:
        x = f"({a[0]},{a[1]}),({b[0]},{b[1]}),({c[0]},{c[1]})"
        t.append(x)
    z = "\n".join(t)+"\n"
    s.send(bytes(z,"utf-8"))
    time.sleep(0.5)
    print(s.recv(4048).decode("utf-8"))




reset()
#mi, mj = 24,50
mark(mi,mj)
fill_all_rows(mi)
fill_all_cols(mi, mj)
mi4 = mi - (mi%3)
mj4 = mj - (mj%3)
if mi4 == mi and mj4 == mj:
    brute_force_16(mi, mj)
    grid()
    send_soluce()
else:
    print("nop")

