import datetime

def calculate_discount(age, is_member, day_of_week):
    """
    Calculate the total discount for a customer based on age, membership status, and day of the week.

    Parameters:
    - age (int): The age of the customer.
    - is_member (bool): True if the customer is a member, False otherwise.
    - day_of_week (str): The current day of the week (e.g., 'Monday', 'Saturday').

    Returns:
    - float: Total discount percentage.
    """
    discount = 0

    # Age-based discount
    if age < 18 or age > 65:
        discount += 20

    # Membership discount
    if is_member:
        discount += 10

    # Weekend discount
    if day_of_week in ['Saturday', 'Sunday']:
        discount += 5

    return discount

def main():
    # Input from the user
    try:
        age = int(input("Enter your age: "))
        is_member = input("Are you a member? (yes/no): ").strip().lower() == 'yes'

        # Get current day of the week
        current_day = datetime.datetime.now().strftime("%A")

        # Calculate discount
        discount = calculate_discount(age, is_member, current_day)

        # Display the result
        print(f"Today is {current_day}.")
        print(f"You are eligible for a {discount}% discount.")
    except ValueError:
        print("Invalid input. Please enter valid details.")

if __name__ == "__main__":
    main()
