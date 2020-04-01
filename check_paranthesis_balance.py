from stack import Stack

def check_parantheses_balance(s):
    opn  = ['{','[','(']
    clse  = ['}',']',')']
    st = Stack()
    for i in range(0, len(s)):
        if s[i] in opn:
            st.push(s[i])
        else:
            if st.isEmpty():
                return "Not balanced"
            else:
                elem = st.pop()
                if elem ==  "(" and s[i] == ")":
                    pass
                elif elem == "{" and s[i] == "}":
                    pass
                elif elem == "[" and s[i] == "]":
                    pass
                else:
                    return "Not balanced"
    if st.isEmpty():
        return "Balanced"
    else:
        return "Not balanced"


s = "{[()()]}"
#s = "(()"
#s = "[][]]]"
print(check_parantheses_balance(s))