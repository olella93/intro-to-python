<!-- datatypes in python -->
<!-- Numbers -->
integer => 1, 2, 3
float => 4.5 , 0.1

<!-- boolean =>bool -->
true
false

<!-- list -->
<!-- mutable -->
numbers = [1, 2, 3, 4]
fruits = []
products = list()

<!-- tuple -->
<!-- immutable -->
num = (1, 2,)

<!-- mutability -->

<!-- dictionary -->
person = {
    "name": "Brian",
    "gender": "Male",
    "isActive": true,
    "age": 21
}

dog = {}
car = dict()

<!-- set -->

<!-- string -->

name = "Hello world"

<!-- arithemetic operation -->
addition +
modular %
subtruction -
division /
// floor  3//2 => 1
multiplication *

<!-- comparison operators -->
>
<
=>
<=
== loose
=== strict equality

1 == "1"  true
1 === "1"  false

<!-- assignment operands -->
=
++
--
count++   count +=1
count--   count -=1

<!-- logical operation -->
OR   
AND  
NOT

1 or 2
3 and 4
4 not 6

age = 16
name = "Seth"

if(age > 18 or name === "Seth"){
    print("Hello there")
}
else{
    print("You are joking")
}

<!-- conditional statement -->
if
else if 

else

if condition1:
elif condition2:
elif condition3:
else:

while

<!-- variable -->
name = "Kevin"


<!-- function -->
<!-- function greetings(){

} -->

def greetings():

<!-- sequence -->
string
range
list => ordered and changeable
tuple => ordered and unchangeable

fruits = ["apple", "mango", "orange"]
fruit[0]


set => unordered and immutable, allows addition and removal of items. doesn't allow duplicates

dictionary => unodered and changeable



<!-- intro to oop -->
class => data::attribute and functionalities::methods::behaviours

vehicle => attributes:: model, year, brand
           behviours(methods): start, stop

           <!-- object/instance -->
           Nissan Note
           Demio
           Bugati

person => attributes:: name, gender, age, height
        methods: sleep, walk, run

        <!-- instances -->
        person_1
        person_2

<!-- attribute -->
<!-- instance attributes -->
affects a particular instance
demio.brand
person_1.age

<!-- class attributes -->
affects the whole class

<!-- methods -->
<!-- instance methods -->
affect an instance
demio.start()
person_1.run()

<!-- class methods -->
applicable on a class
student_count
Vehicle.student_count()