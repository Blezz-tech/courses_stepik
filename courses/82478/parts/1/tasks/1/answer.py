def check(text):
    stack = []

    for i, x in enumerate(text, 1):
        if (x in "{[("):
            stack.append(i)
        elif (x in "}])"):
            if (not stack):
                return i
            s = text[stack.pop() - 1]
            if (s + x not in ["[]", "{}", "()"]):
                return i
    if (stack):
        return stack.pop()
    return "Success"

print(check(input()))


# Для проверки, в решение не входит

assert check("([](){([])})") == "Success"
assert check("()[]}") == 5
assert check("{{[()]]") == 7
assert check("{{{[][][]") == 3
assert check("{*{{}") == 3
assert check("[[*") == 2
assert check("{*}") == "Success"
assert check("{{") == 2
assert check("{}") == "Success"
assert check("") == "Success"
assert check("}") == 1
assert check("*{}") == "Success"
assert check("{{{**[][][]") == 3
