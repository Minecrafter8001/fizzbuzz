def fizzbuzz(rules, start,end):
    for i in range(start, end+1):
        output = ''
        for condition, word in rules:
            if eval(condition, {'x': i}):
                output += word
        print(f'{i}. {output}' if output else f'{i}')

# Example usage:
rules = [
    ('x % 5 == 0', 'fizz'),
    ('x % 3 == 0', 'buzz'),
    ('x % 7 == 0', 'pop'),
]

fizzbuzz(rules, 1,100)
