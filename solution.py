# Case Study 29: Password Policy Validation Engine

def validate_password(password):
    failures = []

    if len(password) < 8:
        failures.append("Must contain at least 8 characters.")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        else:
            has_special = True

    if not has_upper:
        failures.append("Must contain an uppercase letter.")
    if not has_lower:
        failures.append("Must contain a lowercase letter.")
    if not has_digit:
        failures.append("Must contain a digit.")
    if not has_special:
        failures.append("Must contain a special character.")

    repeated = False
    for index in range(len(password) - 2):
        if password[index] == password[index + 1] == password[index + 2]:
            repeated = True
    if repeated:
        failures.append("Must not contain 3 identical consecutive characters.")

    if "password" in password.lower():
        failures.append("Must not contain the prohibited word 'password'.")

    return failures


def main():
    samples = ["Niat@2026", "abc123", "PasswoRD123!", "Aa1111!xy"]
    print("PASSWORD POLICY VALIDATION")
    print("-" * 48)
    for sample in samples:
        failures = validate_password(sample)
        print(f"Password: {sample}")
        if failures:
            print("Result: INVALID")
            for failure in failures:
                print(f"  - {failure}")
        else:
            print("Result: VALID")
        print()


if __name__ == "__main__":
    main()
