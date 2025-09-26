def main():
    number = int(input('Enter an integer number'))
    if number % 2 == 0:
        result = 0
    else:
        result = 1
    
    if result:
        print(f'The value {number} is an odd number')
    else:
        print(f'The value {number} is an even number')
    return result


if __name__ == '__main__':
    main()
