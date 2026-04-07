def grade(output, expected):
    if output == expected:
        return 1.0
    elif output in expected:
        return 0.5
    else:
        return 0.0