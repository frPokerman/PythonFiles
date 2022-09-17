def maybe(condition, onTrue, onFalse):
    return {True: onTrue, False: onFalse}[condition]

def stringify(array, separator = " "):
    stringed = ""
    keepIndex = -1
    for i in array:
        keepIndex += 1
        stringed += i
        if keepIndex < len(array) - 1:
            stringed += separator
    return stringed

def Input(askMessage, errorMessage, authMode):
    while True:
        print(askMessage, end="")
        response = input()
        if "/" in authMode:
            cdn = authMode[0] == "^"
            for auth in maybe(cdn, authMode[1:], authMode).split("/"):
                if auth == response:
                    return response
                elif not cdn and response.lower() == auth.lower()[:len(response)]:
                    return response
        elif (".." in authMode and authMode.replace("..", "") != "") or ("..." in authMode and authMode.replace("...", "") != ""):
            points = maybe(".." in authMode and not "..." in authMode, "..", "...")
            min = "null"
            max = "null"
            index = authMode.index(points)
            d = authMode[:index]
            if d != "":
                try:
                    if len(points) == 3:
                        min = float(d)
                    else:
                        min = int(d)
                except:
                    print(f"-- Error in script ({authMode[:index]} is not a bound)")
            d = authMode[index + len(points):]
            if d != "":
                try:
                    if len(points) == 3:
                        max = float(d)
                    else:
                        max = int(d)
                except:
                    print(f"-- Error in script ({d} is not a bound)")
            try:
                if min != "null" and max != "null":
                    if float(response) <= max and float(response) >= min:
                        if len(points) == 3:
                            return float(response)
                        else:
                            return int(response)
                elif min == "null" and max != "null":
                    if float(response) <= max:
                        if len(points) == 3:
                            return float(response)
                        else:
                            return int(response)
                elif min != "null" and max == "null":
                    if float(response) >= min:
                        if len(points) == 3:
                            return float(response)
                        else:
                            return int(response)
                else:
                    print("-- Error in script (Both bounds of range were null)")
            except:
                error = "-1"
        elif authMode.lower() == "*n":
            isLegit = True
            for c in response.lower():
                if not ((ord(c) >= 97 and ord(c) <= 122) or ord(c) in {32, 45}):
                    isLegit = False
            if isLegit:
                return response
        elif authMode.lower() == "*d":
            try:
                return int(response)
            except:
                error = "-1"
        elif authMode.lower() == "*f":
            try:
                return float(response)
            except:
                error = "-1"
        elif authMode.lower() == "path":
            import os
            if os.path.exists(response):
                return response
        elif authMode.lower() == "dir":
            import os
            if os.path.isdir(response):
                return response
        elif "|" in authMode and authMode.split("|")[0] != "" and authMode.split("|")[1] != "":
            import os
            if os.path.isfile(response):
                name = os.path.basename(response)
                n = authMode.split("|")[0]
                ext = authMode.split("|")[1]
                if (n == name.split(".")[0] or n == "*") and ((stringify(name.split(".")[len(name.split(".")) - 1 - ext.count("."):], ".") == ext) or ext == "*"):
                    return response
        else:
            print("-- Error in script (could not determine selector)")
        if errorMessage != "":
            print(errorMessage)
