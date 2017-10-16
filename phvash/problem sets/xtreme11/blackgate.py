"""
6
TheJoker 180
HarleyQuin 160
MrHammer 220
Boody 220
Muggs 180
Paulie 180
"""

def main():
    n = int(input())
    heights = []
    dicx = {}
    num_dic = {}
    
    for i in range(n):
        name, height = input().strip(" ").split(" ")
        height = int(height)
        heights.append(height)
        names = dicx.get(height, [])
        previous_count = num_dic.get(height, 0)
        count = previous_count + 1
        num_dic[height] = count
        names.append(name)
        dicx[height] = sorted(names)
        
    heights = sorted(heights)

    for i in sorted(dicx.keys()):
        min_p = heights.index(i) + 1
        max_p = min_p + num_dic[i] - 1
        print(' '.join(dicx[i]), min_p, max_p)
        
if __name__ == '__main__':
    main()
        