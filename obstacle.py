height=int(input('Enter the height of the pyramid: '))

def mario_pyramid(height):
    while height > 23 or height < 0:
        height = int(input('Enter an integer between 1 and 23: '))
    if 0 < height <= 23:
        for i in range(int(height)):
            print(' ' * (int(height) - i - 1) + '#' * (i + 2))

print(mario_pyramid(height))