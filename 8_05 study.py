# Boolean

print(True) # 참
print(False) # 거짓

#012
print(0)
if True:
    print(1)
print(2)

print('---')

print(0)
if False:
    print(1)
print(2)

input_id = input('id : ')
id = 'egoing'
if input_id == id:
    print('welcome')


print(0)
if True:
    print(1)
else:
    print(2)
print(3)

# 조건문 else

# 013
print(0)
if True:
    print(1)
else:
    print(2)
print(3)
print('---')
# 013
print(0)
if False:
    print(1)
else:
    print(2)
print(3)

input_id = input ('id : ')
id = 'egoing'
if input_id == id:
    print('welcome')
else:
    print('who?')

# 조건문  elif

print(0)
if True:
    print(1)
elif True:
    print(2)
else:
    print(3)
print(4)
print('---')
#024
print(0)
if False:
    print(1)
elif True:
    print(2)
else:
    print(3)
print(4)

# 조건문 중첩
input_id = input('id :')
id = 'egoing'
input_password = input('password:')
('passwoed:')
password = '111111'
if input_id == id:
    if input_password == password:
        print('welcome')
    else:
        print('wrong password')
else:
    print('wrong id')


input_id = input('id : ')
id1 = 'egoing'
id2 = 'basta'
if input_id == id1:
    print('welcome')
elif input_id == id2:
    print('welcome')
else:
    print('who')

