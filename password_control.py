while True:
    password= input("Please create a password: ")
    error_count=0
    # UPPERCASE CONTROL
    for i in password:
        has_upper= i.isupper()
        if has_upper== True:
            break
        else:
            has_upper=False
    if has_upper==False:
        print("Password must contain at least one uppercase letter.")
        error_count+=1

    # LOWERCASE CONTROL
    for i in password:
        has_lower= i.islower()
        if has_lower== True:
            break 
        else:
            has_lower=False
    if has_lower== False:
        print("Password must contain at least one lowercase letter.")
        error_count+=1

    # NUMBER CONTROL
    for i in password:
        has_digit = i.isdigit()
        if has_digit== True:
            break 
        else:
            has_digit=False
    if has_digit== False:
        print("Password must contain at least one digit.")
        error_count+=1

    if error_count==0:
        print("Password created successfully!")
        break
    else:
        continue



