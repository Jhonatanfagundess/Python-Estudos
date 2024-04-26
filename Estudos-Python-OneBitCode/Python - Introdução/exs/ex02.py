name = 'Fifa 23'
name2 = 'Resident 4'

character = name[0].lower()
character2 = name2[0].lower()

new2 = name2.replace(character2, '#')
new2 = character2 + new2[1:]

new = name.replace(character,'#')
new = character + new[1:]
print(new)
print(new2)

st1 = 'abc'
st2 = 'xyz'

new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]

print(f"{new_st1} {new_st2}")