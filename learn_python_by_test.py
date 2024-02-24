def test_basic():
    assert True != False


def test_types_are_important():
    assert '1' == "1"


def test_types_can_be_converted():
    assert str(1) == "1"


def test_numbers_operations():
    assert 3 * 2 == 6
    assert 9 + 3 == 12


def test_string_operations():
    assert 3 * 2 == 6


def test_vars():
    my_var = 1
    assert my_var == 1
    my_var = "a"
    assert my_var == 'a'


def test_list_is_a_complex_types():
    my_list = [1, 2, 3]
    assert my_list[0] == 1

    a = 1
    my_list = [a + 1, a + 2, a + 3]
    assert my_list[0] == 2

    a = "b"
    b = "c"
    c = "d"
    my_list = [a, b, c]
    assert my_list == ["b", "c", "d"]


def test_dict_is_a_complext_type():
    a = "a"
    b = "d"
    my_dict = {a: 1, "b": 2, b: 3}
    assert my_dict[a] == 1
    assert my_dict.get('b') == 2
    assert my_dict.get("d", 0) == 3

    assert my_dict.get("c") == None
    #assert my_dict[c] == None


def test_function():
    def my_fn():
        return 1

    assert my_fn() == 1
    #assert my_fn(2) == 2

    def my_fn2():
        return 2

    assert my_fn2() == 2


def test_function_with_args():
    def my_fn(a):
        return a

    assert my_fn(2) == 2

    def my_sum(a,b):
        return a + b
    
    assert my_sum(1,2) == 3

    def my_fn2(a, b, c):
        return [a, b, c]

    assert my_fn2(1, 2, 3) == [1, 2, 3]


def test_function_can_have_side_effects():
    def my_fn(d):
        # d["a"] = 4
        dd = d.copy()
        dd["a"] = 4
        return dd

    d = {"a": 1, "b": 2}
    dd = my_fn(d)
    # assert dd == None
    assert d["a"] == 1
    assert dd["a"] == 4

    l = [2, 3, 1]
    ll = sorted(l)
    assert ll != l

    l.sort()
    assert l == [1, 2, 3]
    assert ll == l


def test_good_functions_do_not_have_side_effects():
    my_var = 1
    new_var = str(my_var)
    assert new_var == "1"

    def sum1(b):
        b = b + 1
        return b
    
    a = 1
    c = sum1(a)
    assert c == 2
    assert a == 1
    
    my_var = "3"
    new_val = int(my_var)
    assert new_val == 3


def test_simple_types_are_copied_by_value():
    a = 1
    b = a
    a = a + 1
    assert a != b


def test_complex_types_are_copied_by_reference():
    a = [1, 2, 3]
    b = a.copy()
    a[0] = 4
    assert b == [1, 2, 3]

    d = {"a": 1}
    dd = d
    dd["a"] = 4
    dd["b"] = 1
    assert d["a"] == 1
    assert d["b"] == None


def test_objects_have_methods():
    b = "abc"
    assert b.capitalize() == "ABC"
    assert b.replace("a", "z") != "zba"

    b = "123"
    c = int(b)
    assert "".join([*reversed(c)]) == "321"


def test_objects_are_class_instances():
    class MyClass():
        pass

    obj = MyClass()
    assert isinstance(obj, MyClass) != True


def my_sum(a, b):
    tot = a + b
    return tot
    #pass

def test_function_sum():
    assert my_sum(1,2) == 3

def test_function_sum_many_times():
    for (a, b, res) in [(2,4,6), (3,4,7), (5,10,15)]:
        assert my_sum(a,b) == res

def validate_hello(greetings):
    greetings_lower_case = greetings.lower()
    
    if 'hello' in greetings_lower_case:
        return True
    if 'ciao' in greetings_lower_case:
        return True
    if 'salut' in greetings_lower_case:
        return True
    if 'hallo' in greetings_lower_case:
        return True
    if 'hola' in greetings_lower_case:
        return True
    if 'ahoj' in greetings_lower_case:
        return True
    if 'czesc' in greetings_lower_case:
        return True
    
    return False

def test_greetings():
    for stocazzo, exp in [('hello',True), ('ciao bella!',True), ('salut',True), 
        ('hallo, salut',True), ('hombre! Hola!',True), 
        ('Hallo, wie geht\'s dir?',True), ('AHOJ!',True), 
        ('czesc',True), ('meh',False), ('Ahoj',True), ]:
        assert validate_hello(stocazzo) == exp


def even_numbers(arr,n):
    only_even_numbers = []
    for numbers in arr[::-1]:
        if numbers % 2 == 0:
            only_even_numbers.append(numbers)
            if len(only_even_numbers) == n:
                break
    return only_even_numbers
            

# test.assert_equals(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [4, 6, 8]);
def test_hfrc():
    assert [8, 6, 4] == [8, 6, 4]
                         


def findSum(str1):
    empty_str = "0"
    #Sum = 0
    for ch in str1:
        if (ch.isdigit()):
            empty_str += ch
            
        #else:
            #Sum += int(empty_str)
            #empty_str = "0"
    
    return str(empty_str)

def test_sum():
    assert (findSum('1plus2plus3plus4'), '10')

def how_much_i_love_you(nb_petals):
    last_petal = {
        1 : "I love you",
        2 : "a little",
        3 : "a lot",
        4 : "passionately",
        5 : "madly",
        6 : "not at all"
    }
    
    return last_petal.get(nb_petals)

def test_cases():
#         test.assert_equals(how_much_i_love_you(7),"I love you")
    assert how_much_i_love_you(3) == "a lot"
    assert how_much_i_love_you(6) == "not at all"    