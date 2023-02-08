if __name__ == '__main__':
    s = input()

    # any (iterable) ---> if iterable contains atleast 1 true... Returns True ===> 6 false, 1 true ---> returns true
    # unpacking using list comprehension: newlist = [x for x in fruits if "a" in x]
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))
