calls = 0
def count_calls():
    global calls
    return calls
def string_info(string):
    global calls
    calls += 1
    # string = 'RuZa'
    up_ = string.upper()
    low_ = string.lower()
    cort_ = (len(string), string.upper(), string.lower())
    return cort_
def is_contains(string, list_to_search):
    global calls
    calls += 1
    string = string.upper()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].upper()
    print(list_to_search)

    return string in list_to_search

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)


