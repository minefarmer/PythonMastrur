'''                 Variables

Variables are memory location references which store values.
    Address to values in my computer's memory.

my_message               =          'Hello World using single quotes'.
    |                    |                   |       
memory location     assignment operator  string to be referenced



'''

my_message = 'Hello World using single quotes.'
print(my_message)  # Hello World using single quotes.




'''                 Strings
        Concatenation, indexing, slicing.



'''

message = "The price of the stock is:"
price = "$1100"
print(message + " " + price)  # The price of the stock is: $1100


message = "The price of the stock is: "
price = "$1100"
print(message + price)  # The price of the stock is: $1100


new_message = message + price
print(new_message)  # The price of the stock is: $1100
print(id(message))  # 2015286636912


price = 
new_message = message + price
print(new_message)  # The price of the stock is: $1100
print(id(message))  # 2015286636912
