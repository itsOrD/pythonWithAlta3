#!/usr/bin/python3
''' itsOrD || more input practice '''


def main():
    '''multiple inputs accepted and concat'd'''
    user_name = input(f'''Who there? ''').capitalize()
    day = input(f'''Oh really {user_name}?  Prove it. What's the day of the week? ''')
    print(f'''Oh nice. Hey {user_name}. Great to see you this beautiful {day.capitalize()}.''')


if __name__ == "__main__":
    main()
