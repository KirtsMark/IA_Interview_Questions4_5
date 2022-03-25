def idchecker():
    idstring = input('Enter elements of a list: ')
    success = False
    error_code = "001"
    error_message = ""
    idval=[]
    for i in idstring:
        if (i == "" or i.isdigit() == False):
            error_message = "citizen_id require"
            print(success, error_code, error_message)
            return 
        idval.append(int(i))
    if (len(idval) != 13):
        error_message = "citizen_id invalid"
        print(success, error_code, error_message)
        return
    idval.pop()
    print(idval)
    newid = []
    idval.reverse()
    for i in range(len(idval),1,-1):
        val = (i+1) * idval[i-1]
        newid.append(val)
    idtotal = sum(newid)%11
    check_digit = 11 - idtotal
    if (check_digit>=10):
        check_digit = check_digit%10
    success = True
    error_code = "200"
    error_message = ""
    print(success, error_code, error_message)
    return success, error_code, error_message 

idchecker()
