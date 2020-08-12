#!/sr/bin/python3
''' itsOrD || asterisk pyramid with for loops '''


def main():
    '''print sideways *'s in a pattern'''
    stars = ''
    for i in range(0, 9):
        if i < 5:
            stars += '* '
        elif i >= 5:
            stars = stars[:-2]
        print(stars)


if __name__ == "__main__":
    main()
