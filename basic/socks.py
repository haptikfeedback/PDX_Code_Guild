import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_colors = ['black', 'white', 'blue']
socks = []
colors = []
colors_count = {}
socks_count = {}

def sockType():
    for i in range(100):
        socks.append(random.choice(sock_types))

    for sock in socks:
        if sock in socks_count.keys():
            socks_count[sock] += 1
        else: 
            socks_count[sock] = 1

    for sock, count in socks_count.items():
        if count % 2 != 0:
            print(f'{sock} has 1 loner')
    # print(socks_count)

def sockColor():
    for i in range(100):
        colors.append(random.choice(sock_colors))
    

    for color in colors:
        if color not in socks_count.values():
            socks_count[color].append(color) 

    print(color)
    print(socks_count)
    


# def combineSocks():


sockType()
sockColor()