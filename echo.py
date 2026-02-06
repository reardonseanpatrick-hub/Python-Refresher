# echo.py

def echo(text: str, repetitions: int = 3) -> str:
    result = []
    current = text[-3:]

    for _ in range(repetitions):
        result.append(current)
        current = current[1:]

    result.append(".")
    return "\n".join(result)


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
