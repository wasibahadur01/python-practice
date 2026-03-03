def http_status_code(status: int) -> str:
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status Code"
# Example usage
print(http_status_code(200))  # Output: OK
print(http_status_code(404))  # Output: Not Found
print(http_status_code(500))  # Output: Internal Server Error