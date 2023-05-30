import pandas as pd

def get_node_level(x):
    return x.count('.')

def change_level(x:str, level:int):
    levels = x.split('.')
    return ".".join(levels[0:level])





if __name__ == '__main__':
    print(change_level('level.node', level=1))
    print(change_level('level.node', level=3))
    
