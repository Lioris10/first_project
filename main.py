import argparse
## from goodbye import finish
import goodbye


def greet(name):
    """
    Function to greet a person by name.
    """
    return f"Hello, {name}!"


def add(a, b):
    """
    Function to add two numbers.
    """
    return a + b


def main():
    print("Hello Word")
    """
    Main function that gets executed when the script is run.
    """
    parser = argparse.ArgumentParser(description="Example script with functions.")
    parser.add_argument('name', type=str, help="Your name")
    parser.add_argument('num1', type=int, help="First number")
    parser.add_argument('num2', type=int, help="Second number")

    args = parser.parse_args()

    greeting = greet(args.name)
    print(greeting)

    result = add(args.num1, args.num2)
    print(f"The sum of {args.num1} and {args.num2} is {result}.")

    ## bye_message = finish(args.name)
    bye_message = goodbye.finish(args.name)
    print(bye_message)


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


if __name__ == "__main__":
    main()