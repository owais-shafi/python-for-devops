## What is a Lambda Function?
Lambda functions are similar to user-defined functions but without a name. They're commonly referred to as anonymous functions.

Lambda functions are efficient whenever you want to create a function that will only contain simple expressions – that is, expressions that are usually a single line of a statement. They're also useful when you want to use the function once.

## How to Define a Lambda Function
You can define a lambda function like this:

lambda argument(s) : expression
lambda is a keyword in Python for defining the anonymous function.

argument(s) is a placeholder, that is a variable that will be used to hold the value you want to pass into the function expression. A lambda function can have multiple variables depending on what you want to achieve.

expression is the code you want to execute in the lambda function.

Notice that the anonymous function does not have a return keyword. This is because the anonymous function will automatically return the result of the expression in the function once it is executed.

Let's look at an example of a lambda function to see how it works. We'll compare it to a regular user-defined function.

Assume I want to write a function that returns twice the number I pass it. We can define a user-defined function as follows:

def f(x):
  return x * 2

f(3)
>> 6
Now for a lambda function. We'll create it like this:

lambda x: x * 3
As I explained above, the lambda function does not have a return keyword. As a result, it will return the result of the expression on its own. The x in it also serves as a placeholder for the value to be passed into the expression. You can change it to whatever you want.

Now if you want to call a lambda function, you will use an approach known as immediately invoking the function. That looks like this:

(lambda x : x * 2)(3)

>> 6
The reason for this is that since the lambda function does not have a name you can invoke (it's anonymous), you need to enclose the entire statement when you want to call it.

## When Should You Use a Lambda Function?
You should use the lambda function to create simple expressions. For example, expressions that do not include complex structures such as if-else, for-loops, and so on.

So, for example, if you want to create a function with a for-loop, you should use a user-defined function.

## Common Use Cases for Lambda Functions
# How to Use a Lambda Function with Iterables
An iterable is essentially anything that consists of a series of values, such as characters, numbers, and so on.

In Python, iterables include strings, lists, dictionaries, ranges, tuples, and so on. When working with iterables, you can use lambda functions in conjunction with two common functions: filter() and map().

Filter()
When you want to focus on specific values in an iterable, you can use the filter function. The following is the syntax of a filter function:

filter(function, iterable)
As you can see, a filter function requires another function that contains the expression or operations that will be performed on the iterable.

For example, say I have a list such as [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Now let's say that I’m only interested in those values in that list that have a remainder of 0 when divided by 2. I can make use of filter() and a lambda function.

Firstly I will use the lambda function to create the expression I want to derive like this:

lambda x: x % 2 == 0
Then I will insert it into the filter function like this:

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter(lambda x: x % 2 == 0, list1)

>> <filter at 0x1e3f212ad60> # The result is always filter object so I will need to convert it to list using list()

list(filter(lambda x: x % 2 == 0, list1))
>> [2, 4, 6, 8, 10]
Map()
You use the map() function whenever you want to modify every value in an iterable.

map(function, iterable)
For example, let's say I want to raise all values in the below list to the power of 2. I can easily do that using the lambda and map functions like this:

list1 = [2, 3, 4, 5]

list(map(lambda x: pow(x, 2), list1))
>> [4, 9, 16, 25]
<!-- another example -->
double = lambda x : x*2
print(double(2))   
<!-- how did we put braces'()' in 'double()' because inside double there a function(lambda function) itself thats why we are able to write double(2) --> 