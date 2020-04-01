def generate_permutations(text):
    if text is None:
        return None

    if len(text) == 0:
        return [""]

    results = []
    first = text[0]
    remainder = text[1:]

    words = generate_permutations(remainder)

    for word in words:
        for i in range(0, len(word)+1):
            s = word[:i] + first + word[i:]
            results.append(s)
    return results 
    

print(generate_permutations("abc"))

def gen_perms(text):
    if len(text) == 0:
        return [""]

    results = []
    for i in range(0, len(text)):
        exclude = text[i]
        include = text[:i] + text[i+1:]
        words = gen_perms(include)
        for word in words:
            results.append(exclude+word)
        
    return results

a = (gen_perms("hello"))
print(a)

def gen_perms_with_dups(text):
    if len(text) == 0:
        return [""]
    
    results = []
    for idx in range(0, len(text)):
        exclude = text[idx]
        include = text[0:idx] + text[idx+1:]
        words = gen_perms_with_dups(include)
        for word in words:
            if exclude+word not in results:
                results.append(exclude+word)
    return results

b = (gen_perms_with_dups("hello"))

def gen_perms_with_dups_1(text_counter, prefix, remaining, results):
    if remaining == 0:
        results.append(prefix)
        return results

    for key in text_counter:
        count = text_counter[key]
        if count > 0:
            text_counter[key] -= 1
            gen_perms_with_dups_1(text_counter, prefix+key, remaining-1, results)
            text_counter[key] = count
    return results

from collections import Counter
def perms(text):
    text_counter = Counter(text)
    results = []
    results = gen_perms_with_dups_1(text_counter, "", len(text), results)
    return results

results = perms("hello")


        