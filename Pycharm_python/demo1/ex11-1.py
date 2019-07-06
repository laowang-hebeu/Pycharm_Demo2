while True:
    x = input('Pls input:')
    try:
        x = int(x)
        print('You have input {0}'.format(x))
        break
    except Exception as e:
        print('Error.')

