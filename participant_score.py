def participant_score():
    '''
    Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
    You are given  scores. Store them in a list and find the score of the runner-up.
    :return: Runner up
    '''
    while True:
        # Loop to ensure the number of participants (n) is between 2 and 10
        n = int(input("Enter the number of participants:"))

        # Check if the entered number is within the valid range
        if 2 <= n <= 10:
            break
        else:
            # If not valid, print an error message and prompt again
            print("InvalidNumber: Please enter an integer between 2 and 10.")
    # Loop to ensure the user enters exactly n numbers
    while True:

        arr = input(f"Enter {n} numbers separated by a spaces:").strip()
        scores = list(map(int, arr.split()))
        if len(scores) == n:
            break
        else:
            print(f"InvalidList: Please enter {n} numbers separated by spaces.")

    # Convert the list of scores to a set to remove duplicates
    unique_scores = set(scores)

    # Sort the unique scores in descending order
    sorted_scores = sorted(unique_scores, reverse = True)

    print(sorted_scores[1])


participant_score()