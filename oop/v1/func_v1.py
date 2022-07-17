from datetime import datetime

def greet(name: str, greeting_intro: str) -> str:
    return f"{greeting_intro}, {name}"

def greet_list(names: list[str], greeting_intro: str) -> list[str]:
    return [greet(name, greeting_intro) for name in names]

def read_greeting() -> str:
    current_time = datetime.now()
    if current_time.hour < 12:
        return "Good morning"
    elif 12 <= current_time.hour:
        return "Good afternoon"
    else:
        return "Good evening"

def read_name() -> str:
    return input("Enter your name: ")

def main() -> None:
    print(greet(read_name(), read_greeting()))
    print(greet_list(["John", "Jane", "Mary"], read_greeting()))

if __name__ == "__main__":
    main()