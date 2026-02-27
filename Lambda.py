# def my_function(args):
#     return lambda a:a * args;
# b=my_function(2);
# print(b(4));

# numbers = [1, 2, 3, 4, 5]
# doubled = list(map(lambda x: x * 2, numbers));
# # a=[x *2 for x  in numbers]
# print(doubled);

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers =list((lambda b:b%2 !=0,numbers))
print(odd_numbers)