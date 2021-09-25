# banking_system

## Stage 1: Card anatomy

### Description
In this project, you will develop a simple banking system with a database.
Let's take a look at the anatomy of a credit card:
* The very first digit is the Major Industry Identifier (MII), which tells you what sort of institution issued the card. In our banking system, credit cards should begin with 4.
* The first six digits are the Issuer Identification Number (IIN). These can be used to look up where the card originated from. If you have access to a list that provides detail on who owns each IIN, you can see who issued the card just by reading the card number. In our banking system, the IIN must be 400000.
* The seventh digit to the second-to-last digit is the customer account number. Most companies use just 9 digits for the account numbers, but it’s possible to use up to 12. In our banking system, the customer account number can be any, but it should be unique. And the whole card number should be 16-digit length.
* The very last digit of a credit card is the check digit or checksum. It is used to validate the credit card number using the Luhn algorithm, which we will explain in the next stage of this project.

### Objectives
You should allow customers to create a new account in our banking system.

Once the program starts, you should print the menu:
- [x] `1. Create an account`
- [x] `2. Log into account`
- [x] `0. Exit`

If the customer chooses ‘Create an account’, you should generate a new card number which satisfies all the conditions described above. Then you should generate a PIN code that belongs to the generated card number. The PIN code is a sequence of any 4 digits. PIN should be generated in a range from 0000 to 9999.

If the customer chooses ‘Log into account’, you should ask them to enter their card information. Your program should store all generated data until it is terminated so that a user is able to log into any of the created accounts by a card number and its pin. You can use an array to store the information.

After all information is entered correctly, you should allow the user to check the account balance; right after creating the account, the balance should be 0. It should also be possible to log out of the account and exit the program.

## Stage 2: Luhn algorithm

### Description

The main purpose of the check digit is to verify that the card number is valid. Say you're buying something online, and you type in your credit card number incorrectly by accidentally swapping two digits, which is one of the most common errors. Another purpose of the check digit is to catch clumsy attempts to create fake credit card numbers.

The Luhn algorithm is used to validate a credit card number or other identifying numbers, such as Social Security. The Luhn algorithm, also called the Luhn formula or modulus 10, checks the sum of the digits in the card number and checks whether the sum matches the expected result or if there is an error in the number sequence. After working through the algorithm, if the total modulus 10 equals zero, then the number is valid according to the Luhn method.

### Objectives
You should allow customers to create a new account in our banking system.

Once the program starts you should print the menu:

`1. Create an account`

`2. Log into the account`

`0. Exit`

- [x] If the customer chooses ‘Create an account’, you should generate a new card number that satisfies all the conditions described above. Then you should generate a PIN code that belongs to the generated card number. The PIN is a sequence of 4 digits; it should be generated in the range from 0000 to 9999.

- [x] If the customer chooses ‘Log into account’, you should ask to enter the card information.

- [x] After the information has been entered correctly, you should allow the user to check the account balance; after creating the account, the balance should be 0. It should also be possible to log out of the account and exit the program.

## Stage 3: I'm so lite

### Description

It's very upsetting when the data about registered users disappears after the program is completed. To avoid this problem, you need to create a database where you will store all the necessary information about the created credit cards.

### Objectives
- [x] In this stage, create a database named card.s3db with a table titled card. It should have the following columns:

    * id INTEGER
    * number TEXT
    * pin TEXT
    * balance INTEGER DEFAULT 0

## Stage 4:Advanced system

### Description
You have created the foundation of our banking system. Now let's take the opportunity to deposit money into an account, make transfers and close an account if necessary.

Now your menu should look like this:

`1. Balance`

`2. Add income`

`3. Do transfer`

`4. Close account`

`5. Log out`

`0. Exit`


### Objectives

- [x] If the user asks for `Balance`, you should read the balance of the account from the database and output it into the console.

- [x] `Add income` item should allow us to deposit money to the account.

- [x] `Do transfer` item should allow transferring money to another account. You should handle the following errors:

- [x] If the user tries to transfer more money than he/she has, output: `Not enough money!`
- [x] If the user tries to transfer money to the same account, output the following message: `You can't transfer money to the same account!`
- [x] If the receiver's card number doesn’t pass the Luhn algorithm, you should output: `Probably you made a mistake in the card number. Please try again!`
- [x] If the receiver's card number doesn’t exist, you should output: `Such a card does not exist.`
- [x] If there is no error, ask the user how much money they want to transfer and make the transaction.
- [x] If the user chooses the `Close account` item, you should delete that account from the database.

