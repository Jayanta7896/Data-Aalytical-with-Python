#	Dictionary and counter in Python to find winner of election
from collections import Counter

def find_winner(votes):
    # Use Counter to count the votes
    vote_count = Counter(votes)

    # Find the candidate with the maximum votes
    winner = vote_count.most_common(1)[0][0]

    return winner

# Example usage:
votes = ['Candidate A', 'Candidate B', 'Candidate A', 'Candidate C', 'Candidate A', 'Candidate B']

winner = find_winner(votes)

print(f"The winner of the election is: {winner}")
