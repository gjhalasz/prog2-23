import sys
from typing import NamedTuple

Minion = NamedTuple("Minion", [("name", str), ("hunger", int), ("motivation", int), ("size", str)])

def read_minions_stdin() -> list[Minion]:
    minions = []
    for line in sys.stdin:
        #print (line+"$")
        #print (line.strip()+"@")
        tokens = line.strip().split(";")
        minions.append(Minion(tokens[0], int(tokens[1]), int(tokens[2]), tokens[3]))
    return minions

def my_sort(x):
    return (-x.motivation,x.name)

def sort_minions(minions):
    minions.sort(key=my_sort,reverse=False)

def distinct_motivations(minions):
    d_m=set()
    for x in minions:
        d_m = d_m | {x.motivation}
    return d_m

def distinct_sizes(minions):
    d_s=set() # esetleg set("") vagy  set([]),
    # de nem d_s={}, mert ez üres szótárat eredményez
    for x in minions:
        d_s.add(x.size)
    return d_s

def count_by_sizes(minions):
    cbs={}
    for x in minions:
        cbs[x.size]=cbs.get(x.size,0)+1
    return cbs

def count_by_sizes2(minions):
    cbs={}
    for x in minions:
        if not x.size in cbs:
            cbs[x.size]=0
        cbs[x.size]+=1
    return cbs

def count_by_motivations(minions):
    cbm={}
    for x in minions:
        if x.motivation in cbm:
            cbm[x.motivation]+=1
        else:
            cbm[x.motivation]=1
    return cbm

def count_by_motivations2(minions):
    cbm={}
    for x in minions:
        try:
            cbm[x.motivation]+=1
        except KeyError:
            cbm[x.motivation]=1
    return cbm

def group_by_sizes(minions):
    gbs={}
    for x in minions:
        if not x.size in gbs:
            gbs[x.size]=[]
        gbs[x.size].append(x)
    return gbs

def group_by_sizes2(minions):
    gbs={}
    for x in minions:
        if x.size in gbs:
            gbs[x.size].append(x)
        else:
            gbs[x.size]=[x]
    return gbs

def main():
    minions=read_minions_stdin()
    sort_minions(minions)
    for x in minions:
        print(x.name,x.motivation)
    print(distinct_motivations(minions))
    print(distinct_sizes(minions))
    print(count_by_sizes(minions))
    print(count_by_sizes2(minions))
    print(count_by_motivations(minions))
    print(count_by_motivations2(minions))
    print(group_by_sizes(minions))
    print(group_by_sizes2(minions))

if __name__ == "__main__":
        main()