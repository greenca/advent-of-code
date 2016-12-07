import md5

def findPassword(doorID):
    password = ''
    index = 0

    while len(password) < 8:
        cur_hash = md5.new(doorID + str(index)).hexdigest()
        if cur_hash[:5] == '00000':
            password += cur_hash[5]
        index += 1

    return password

def findBetterPassword(doorID):
    password = []
    for i in range(8):
        password.append('')
    index = 0

    while '' in password:
        cur_hash = md5.new(doorID + str(index)).hexdigest()
        if cur_hash[:5] == '00000':
            if cur_hash[5] in '01234567' and password[int(cur_hash[5])] == '':
                password[int(cur_hash[5])] = cur_hash[6]
        index += 1

    return ''.join(password)


if __name__=="__main__":
    print findPassword('abc') == '18f47a30'
    print findPassword('uqwqemis')
    print findBetterPassword('abc') == '05ace8e3'
    print findBetterPassword('uqwqemis')
