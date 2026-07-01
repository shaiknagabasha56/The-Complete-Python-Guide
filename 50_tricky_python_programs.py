

# ============================================================
# SECTION 2: STRING & NUMBER TRICKS
# ============================================================

# 11. Reverse a string without slicing - build it manually using a loop
def reverse_string(s):
    result = ""
    for ch in s:
        result = ch + result
    return result

print(reverse_string("hello"))   # olleh


# 12. Palindrome check ignoring case/spaces - normalize before comparing
def is_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("A man a plan a canal Panama"))  # True


# 13. Count vowels and consonants - filter using a vowel set
def count_vowels_consonants(s):
    vowels = set("aeiouAEIOU")
    v = sum(1 for ch in s if ch.isalpha() and ch in vowels)
    c = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
    return v, c

print(count_vowels_consonants("Hello World"))  # (3, 7)


# 14. f-string vs .format() vs % - three ways to format the same string
name, age = "Sam", 30
print(f"{name} is {age}")
print("{} is {}".format(name, age))
print("%s is %d" % (name, age))


# 15. Float precision issue - binary floating point can't represent 0.1/0.2 exactly
print(0.1 + 0.2 == 0.3)            # False
print(round(0.1 + 0.2, 1) == 0.3)  # True


# 16. Swap two variables without temp - tuple unpacking does it in one line
a, b = 5, 10
a, b = b, a
print(a, b)                        # 10 5


# 17. Check prime number - only test divisors up to sqrt(n) for efficiency
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(29))                # True
print(is_prime(15))                # False


# 18. Find missing number 1 to n - use sum formula instead of looping/searching
def find_missing(nums, n):
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)

print(find_missing([1, 2, 4, 5], 5))  # 3


# 19. Find duplicates using a set - track seen elements in one pass
def find_duplicates(lst):
    seen, dupes = set(), set()
    for x in lst:
        if x in seen:
            dupes.add(x)
        seen.add(x)
    return dupes

print(find_duplicates([1, 2, 3, 2, 4, 1]))  # {1, 2}


# 20. Anagram check - sorted characters of both strings must match
def is_anagram(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

print(is_anagram("listen", "silent"))  # True


# ============================================================
# SECTION 3: LIST/DICT/SET COMPREHENSION CURVEBALLS
# ============================================================

# 21. Flatten a nested list - recursive comprehension handles arbitrary depth
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, 3, [4, [5, 6]]], 7]))  # [1, 2, 3, 4, 5, 6, 7]


# 22. Common elements between two lists - set intersection is the fastest approach
def common_elements(l1, l2):
    return list(set(l1) & set(l2))

print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]


# 23. Remove duplicates preserving order - dict.fromkeys preserves insertion order (3.7+)
def dedupe_ordered(lst):
    return list(dict.fromkeys(lst))

print(dedupe_ordered([3, 1, 3, 2, 1, 4]))  # [3, 1, 2, 4]


# 24. Invert a dictionary - swap keys and values via comprehension
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)                     # {1: 'a', 2: 'b', 3: 'c'}


# 25. Conditional list comprehension - if/else placement differs from filtering if
nums = [1, 2, 3, 4, 5]
labeled = ["even" if n % 2 == 0 else "odd" for n in nums]
evens_only = [n for n in nums if n % 2 == 0]
print(labeled)
print(evens_only)


# 26. Merge two dictionaries - three common ways, including the modern '|' operator
d1, d2 = {"a": 1, "b": 2}, {"b": 3, "c": 4}
merged_unpack = {**d1, **d2}
merged_update = d1.copy(); merged_update.update(d2)
merged_pipe = d1 | d2
print(merged_pipe)             # {'a': 1, 'b': 3, 'c': 4}


# 27. Sort dictionary by value - sorted() with a lambda key on items()
scores = {"alice": 90, "bob": 75, "carl": 85}
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
print(sorted_scores)


# 28. Counter for frequency counting - collections.Counter does it in one line
from collections import Counter
word_counts = Counter("mississippi")
print(word_counts)


# 29. Group items by key - defaultdict avoids manual key-existence checks
from collections import defaultdict
words = ["apple", "banana", "avocado", "blueberry", "cherry"]
grouped = defaultdict(list)
for w in words:
    grouped[w[0]].append(w)
print(dict(grouped))


# 30. Zip two lists into a dict - zip() pairs elements positionally
keys = ["name", "age", "city"]
values = ["Sam", 30, "NYC"]
zipped_dict = dict(zip(keys, values))
print(zipped_dict)


# ============================================================
# SECTION 4: FUNCTIONS, *ARGS/**KWARGS, DECORATORS
# ============================================================

# 31. *args vs **kwargs - *args collects positional args as a tuple, **kwargs as a dict
def show_args(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

show_args(1, 2, 3, name="Sam", age=30)
# args: (1, 2, 3)
# kwargs: {'name': 'Sam', 'age': 30}


# 32. Basic decorator - wraps a function to add behavior (here: timing) without modifying it
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f}s")
        return result
    return wrapper

@timer
def slow_add(a, b):
    time.sleep(0.1)
    return a + b

print(slow_add(2, 3))


# 33. Decorator with arguments - needs an extra outer function to accept the decorator's args
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")

greet()   # prints "Hello!" 3 times


# 34. staticmethod vs classmethod vs instance method - differ in what gets passed automatically
class Demo:
    def instance_method(self):
        return f"instance method, self={self}"

    @classmethod
    def class_method(cls):
        return f"class method, cls={cls}"

    @staticmethod
    def static_method():
        return "static method, no auto args"

d = Demo()
print(d.instance_method())
print(Demo.class_method())
print(Demo.static_method())


# 35. Recursive vs iterative Fibonacci - recursive is elegant but exponential time without memoization
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib_recursive(10))   # 55
print(fib_iterative(10))   # 55


# 36. Memoization with lru_cache - caches return values to avoid recomputation
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

print(fib_memo(50))   # instant, vs very slow without memoization


# 37. Generator vs list - generators yield lazily, using far less memory for large sequences
def squares_list(n):
    return [i * i for i in range(n)]   # builds the whole list in memory

def squares_gen(n):
    for i in range(n):
        yield i * i                     # yields one value at a time

print(sum(squares_list(5)))
print(sum(squares_gen(5)))


# 38. yield vs return - yield pauses the function and resumes later, return ends it immediately
def gen_demo():
    yield 1
    yield 2
    yield 3

g = gen_demo()
print(next(g), next(g), next(g))   # 1 2 3


# 39. Lambda in sorted/map/filter - quick anonymous functions for one-off operations
people = [("Sam", 30), ("Ana", 25), ("Lee", 35)]
print(sorted(people, key=lambda p: p[1]))            # sort by age
print(list(map(lambda x: x * 2, [1, 2, 3])))          # [2, 4, 6]
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))  # [2, 4]


# 40. Return multiple values - Python returns a tuple, which can be unpacked
def min_max(lst):
    return min(lst), max(lst)

low, high = min_max([4, 1, 7, 3])
print(low, high)   # 1 7


# ============================================================
# SECTION 5: OOP & EXCEPTIONS
# ============================================================

# 41. __init__ vs __new__ - __new__ creates the instance, __init__ initializes it after creation
class Demo41:
    def __new__(cls, *args, **kwargs):
        print("__new__ called - creating instance")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print("__init__ called - initializing instance")
        self.value = value

obj = Demo41(10)


# 42. Method Resolution Order (MRO) - determines lookup order in multiple inheritance
class A:
    def greet(self):
        return "A"

class B(A):
    def greet(self):
        return "B"

class C(A):
    def greet(self):
        return "C"

class D(B, C):
    pass

print(D().greet())          # B (follows MRO: D -> B -> C -> A)
print(D.__mro__)


# 43. Operator overloading - dunder methods let custom objects use +, ==, print, etc.
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1, p2 = Point(1, 2), Point(3, 4)
print(p1 + p2)               # Point(4, 6)
print(p1 == Point(1, 2))     # True


# 44. Custom exception class - inherit from Exception to create domain-specific errors
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Cannot withdraw {amount}, balance is only {balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientFundsError as e:
    print(e)


# 45. try/except/else/finally order - else runs only if no exception, finally always runs
def demo_exception_flow(n):
    try:
        result = 10 / n
    except ZeroDivisionError:
        print("except: division by zero")
    else:
        print("else: no error, result =", result)
    finally:
        print("finally: always runs")

demo_exception_flow(2)
demo_exception_flow(0)


# 46. @property vs regular method - property lets a method be accessed like an attribute
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2

c = Circle(5)
print(c.area)   # accessed WITHOUT parentheses, like an attribute


# ============================================================
# SECTION 6: MISC "GOTCHA" QUESTIONS
# ============================================================

# 47. * and ** unpacking in function calls - spread a list/dict into positional/keyword args
def add3(a, b, c):
    return a + b + c

nums_list = [1, 2, 3]
nums_dict = {"a": 1, "b": 2, "c": 3}
print(add3(*nums_list))     # 6, unpacks list as positional args
print(add3(**nums_dict))    # 6, unpacks dict as keyword args


# 48. Slicing tricks - step and negative indices give powerful one-liners
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[::-1])    # reversed
print(lst[::2])      # every 2nd element
print(lst[-3:])      # last 3 elements
print(lst[2:8:2])    # from index 2 to 8, step 2


# 49. is vs == for lists/objects - two equal-looking lists are different objects in memory
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)   # True (same values)
print(list1 is list2)   # False (different objects)
list3 = list1
print(list1 is list3)   # True (same object, just another reference)


# 50. deepcopy vs copy vs assignment - assignment shares reference, copy/deepcopy create new objects
import copy
nested = [[1, 2], [3, 4]]

assigned = nested                  # same object, no copy at all
shallow_copy = copy.copy(nested)   # new outer list, but inner lists still shared
deep_copy_ = copy.deepcopy(nested) # fully independent copy, including inner lists

nested[0][0] = "CHANGED"
print(assigned)       # [['CHANGED', 2], [3, 4]] - affected (same object)
print(shallow_copy)   # [['CHANGED', 2], [3, 4]] - affected (inner list shared)
print(deep_copy_)     # [[1, 2], [3, 4]] - unaffected (fully independent)
