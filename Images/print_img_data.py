with open('bg.png', 'rb') as img:
    raw_bytes = img.read()
    print(' '.join(map(lambda x: '{:08b}'.format(x), raw_bytes)))