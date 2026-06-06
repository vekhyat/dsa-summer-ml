# def outer_function(msg):
   

#     def inner_function():
#         print(msg)
#     return inner_function

def decorator_function(original_function):
    def wrapper_function(*first,**second):
        print(f'{original_function.__name__}')
        return original_function(*first,**second)
    return wrapper_function

@decorator_function
def display():
    print('display ran')
@decorator_function
def display_info(name, age, surname):
    print(f'display_info {name} {age}')

# display()
display_info('Vekhyat',20,'Jain')