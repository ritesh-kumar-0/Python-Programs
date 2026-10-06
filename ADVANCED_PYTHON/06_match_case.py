#match case 

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status" #

print(http_status(200))  # OK
print(http_status(404))  # Not Found
print(http_status(500))  # None 
print(http_status(507))  # Unkon status 