# this is the "test/rps_test.py" file...

from app.rps import determine_winner

def test_example():
    assert 2 + 2 == 4


def test_winner():

    assert determine_winner("rock", "rock") == "TIE GAME"
    assert determine_winner("paper", "paper") == "TIE GAME"
    assert determine_winner("scissors", "scissors") == "TIE GAME"

    assert determine_winner("rock", "paper") == "COMP WINS"
    assert determine_winner("rock", "scissors") == "USER WINS"
    assert determine_winner("paper", "rock") == "USER WINS"
    assert determine_winner("paper", "scissors") == "COMP WINS"
    assert determine_winner("scissors", "paper") == "USER WINS"
    assert determine_winner("scissors", "rock") == "COMP WINS"
