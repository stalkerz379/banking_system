import random
import sqlite3


def create_database():
    try:
        conn = sqlite3.connect("card.s3db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE `card` (`id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, `number` TEXT, `pin` TEXT, `balance` INTEGER DEFAULT 0)")
        conn.commit()
    except sqlite3.OperationalError:
        print('Welcome. You have connected to the banking system! Select one option')


def extract_data_query(query):
    conn = sqlite3.connect("card.s3db")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    result = cursor.fetchall()
    return result


def extract_single_data_query(query, printing=True):
    conn = sqlite3.connect("card.s3db")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    result = cursor.fetchone()
    if printing is True:
        print(*result)
    else:
        return result


def execute_query(query):
    conn = sqlite3.connect("card.s3db")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def banking_system_menu(account_data=None):
    if account_data is None:
        create_database()
        #account_data = extract_data_query('SELECT * FROM card')
    while True:
        user_input = validate_user_option()
        if user_input == 1:
            db_data_recording()
        elif user_input == 2:
            login_into_account()
        else:
            print('Bye!')
            exit()


def db_data_recording():
    card_number = generate_card_number()
    print('Your card number:\n', card_number, sep='')
    pin = generate_pin()
    print(pin)
    query = f'INSERT INTO card (number, pin) VALUES ({card_number}, {pin})'
    execute_query(query)


def login_into_account():
    login_card_num = input('Enter your card number:\n')
    login_pin = input('Enter your PIN:\n')
    account_data = extract_data_query('SELECT * FROM card')
    for instance in account_data:
        if instance[1] == login_card_num and instance[2] == login_pin:
            print("You have successfully logged in!")
            return logging_options(account_data, login_card_num)
        continue
    print("Wrong card number or PIN!")


def logging_options(account_data, card_number):
    logged_options = {'1': 'Balance', '2': 'Add income', '3': 'Do transfer', '4': 'Close account', '5': 'Log out', '0': "Exit"}
    for key in logged_options.keys():
        print(key + '', logged_options[key])
    logging_input_option = input()
    if logging_input_option not in logged_options.keys():
        print('Wrong option')
    elif logging_input_option == '1':
        balance = extract_single_data_query(f"SELECT balance FROM card WHERE number={card_number}", printing=False)
        print("Your current balance is {0}".format(balance[0]))
    elif logging_input_option == '2':
        add_income(card_number)
    elif logging_input_option == '3':
        do_transfer_money(card_number)
    elif logging_input_option == '4':
        close_account(card_number)
        banking_system_menu()
    elif logging_input_option == '5':
        print('You have successfully logged out!')
        banking_system_menu()
    elif logging_input_option == '0':
        print('Bye!')
        exit()
    else:
        print('Wrong option')
        logging_options(account_data, card_number)
    logging_options(account_data, card_number)


def add_income(card_number):
    try:
        new_balance = int(input('Enter income:\n'))
        balance = extract_single_data_query(f"SELECT balance FROM card WHERE number={card_number}", printing=False)
        query = f'UPDATE card SET balance={new_balance + balance[0]} WHERE number={card_number}'
        execute_query(query)
        print('Income was added!')
    except ValueError:
        print('Enter correct income!')


def do_transfer_money(user_card_number):
    card_number = input("Transfer\nEnter card number:\n")
    data_base_cards, option = check_card_for_validity(user_card_number, card_number)
    if option == 1:
        try:
            money_to_transfer = int(input('Enter how much money you want to transfer:'))
            balance = extract_single_data_query(f"SELECT balance FROM card WHERE number={user_card_number}", printing=False)
            print(balance[0])
            if money_to_transfer > balance[0]:
                print('Not enough money!')
            else:
                execute_query(f"UPDATE card SET balance={balance[0] - money_to_transfer} WHERE number={user_card_number}")
                balance_to_transfer = extract_single_data_query(f"SELECT balance FROM card WHERE number={card_number}", printing=False)
                execute_query(f"UPDATE card SET balance={balance_to_transfer[0] + money_to_transfer} WHERE number={card_number}")
                print("Success!")
        except ValueError:
            print('Not enough money!')


def close_account(card_number):
    query = f'DELETE FROM card WHERE number={card_number}'
    execute_query(query)


def validate_user_option():
    options = ["1. Create an account", "2. Log into account", "0. Exit"]
    print('\n'.join(options))
    try:
        user_input = int(input())
        if user_input not in range(0, 3):
            raise ValueError
        return user_input
    except ValueError:
        print('Wrong option, select one option')
        validate_user_option()


def generate_pin():
    pin = ''.join(str(random.choice(range(0, 10))) for x in range(4))
    print('Your card PIN:')
    return pin


def generate_card_number():
    issuer_id_number = '400000'
    customer_acc_number = ''.join(str(random.choice(range(0, 10))) for x in range(9))
    card_number = issuer_id_number + customer_acc_number
    card_numb_sum = validate_card_number(card_number)
    check_sum = get_check_sum_number(card_numb_sum)
    final_card_number = card_number + str(check_sum)
    print('Your card has been created')
    return final_card_number


def get_check_sum_number(card_number_sum):
    check_sum = 0
    while True:
        if (card_number_sum + check_sum) % 10 == 0:
            break
        check_sum += 1
    return check_sum


def validate_card_number(card_number):
    summ = 0
    for ind, char in enumerate(card_number):
        if ind % 2 == 0:
            temp = int(char) * 2
            if temp > 9:
                temp -= 9
            summ += temp
        elif ind % 2 != 0:
            summ += int(char)
    return summ


def check_card_for_validity(user_card_number, transfer_card_number):
    check_sum = validate_card_number(transfer_card_number)
    data_base_cards = extract_data_query("SELECT number FROM card")
    if user_card_number == transfer_card_number:
        print("You can't transfer money to the same account!")
        return data_base_cards, 0
    if check_sum % 10 != 0:
        print("Probably you made a mistake in the card number. Please try again!")
        return data_base_cards, 0
    else:
        for element in data_base_cards:
            if element[0] == transfer_card_number:
                return data_base_cards, 1
        print('Such a card does not exist.')
        return data_base_cards, 0


banking_system_menu()
