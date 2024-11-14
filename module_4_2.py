def test_function():
    def inner_function():
        print('Я в области видимости test_function')
    inner_function()

# вызов inner_function() вне test_function - ошибка, имя не определено.
test_function()
