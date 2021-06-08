from balance import Balance

if __name__ == '__main__':
    check = Balance()
    data_list = [
        '(((([{}]))))',
        '{{[(])]}}',
        '{{[()]}}'
        '}{}'
    ]
    for items in data_list:
        if check.check_balance(items):
            print('Сбалансированно')
        else:
            print('Несбалансированно')
