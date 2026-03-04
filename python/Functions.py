# def my_function(fname,lname,age):
#     print("my name is ", fname,"and my last name is ", lname,"i am", age,"old");
# my_function("test","sample",5)

# def my_function(**kwargs):
#     print("my name is ",kwargs["name"])
#     print("my age is",kwargs["age"])
# sample={"name":"aaa","age":24}
# my_function(**sample);

# def my_function(*imformation):
#     print("my name is ",imformation[0])
#     print("my address is ",imformation[1])
#     print("my pincode is ",imformation[2])
#     print("my pincode is ",imformation[3])
# my_function("sai","India",12345,None);

# def my_function(*args):
#     total=0;
#     for num in args:
#         total += num
#     return total;    

# print(my_function(20,40));
# print(my_function(40,55.4));
# print(my_function(4));

def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num
         

print(my_function(12,3,54,67));