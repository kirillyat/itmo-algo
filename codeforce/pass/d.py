import random

class Node:
    def __init__(self, nx):
        self.x = nx
        self.y = random.random() * random.random()
        self.l = None
        self.r = None

def split(t, x):
    if t is None:
        l = None
        r = None
        return None, None

    if t.x < x:
        t.r, r = split(t.r, x)
        l = t
    else:
        l, t.l = split(t.l, x)
        r = t
    
    return l, r

def merge(l, r):
    if l is None:
        return r
    if r is None:
        return l
    
    if l.y > r.y:
        l.r = merge(l.r, r)
        return l
    else:
        r.l = merge(l, r.l)
        return r

def insert(t, v):
    if t is None:
        return v
    
    if t.y > v.y:
        if v.x < t.x:
            t.l = insert(t.l, v)
        else:
            t.r = insert(t.r, v)
        return t
    
    t.l, t.r = split(t, v.x)
    return v

def remove(t, x):
    if t is None:
        return
    
    if x < t.x:
        t.l = remove(t.l, x)
    elif x > t.x:
        t.r = remove(t.r, x)
    else:
        t = merge(t.l, t.r)
    
    return t

def exists(t, x):
    if t is None:
        return False
    
    if x == t.x:
        return True
    
    if x < t.x:
        return exists(t.l, x)
    else:
        return exists(t.r, x)

def prev(t, x):
    cur = t
    succ = None

    while cur is not None:
        if cur.x < x:
            succ = cur
            cur = cur.r
        else:
            cur = cur.l
    return succ

def next(t, x):
    cur = t
    succ = None

    while cur is not None:
        if cur.x > x:
            succ = cur
            cur = cur.l
        else:
            cur = cur.r
    return succ

t = None

while inn := input():
    try:
        if inn == '':
            break
        s, x = inn.split()
        if s == '':
            break
        x = int(x)

        if s == 'insert':
            v = Node(x)
            if not exists(t, x):
                t = insert(t, v)
        elif s == 'exists':
            if exists(t, x):
                print("true")
            else:
                print("false")
        elif s == 'delete':
            if exists(t, x):
                t = remove(t, x)
        elif s == 'next':
            v = next(t, x)
            if v is None:
                print("none")
            else:
                print(v.x)
        elif s == 'prev':
            v = prev(t, x)
            if v is None:
                print("none")
            else:
                print(v.x)
    except ValueError:
        break
    except EOFError:
        break