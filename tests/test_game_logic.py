from logic_utils import check_guess, get_range_for_difficulty


def test_winning_guess():
    """Test that guessing the exact secret returns Win with correct message"""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    """Test that guessing higher than secret returns Too High with Go LOWER message"""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    """Test that guessing lower than secret returns Too Low with Go HIGHER message"""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_winning_at_boundary_1():
    """Test winning when secret is 1"""
    outcome, message = check_guess(1, 1)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_below_lower_bound():
    """Test that guessing below the lower bound returns Out of Bounds"""
    outcome, message = check_guess(-1, 10, 1, 20)
    assert outcome == "Out of Bounds"
    assert message == "⚠️ Guess must be between 1 and 20!"


def test_guess_above_upper_bound():
    """Test that guessing above the upper bound returns Out of Bounds"""
    outcome, message = check_guess(21, 10, 1, 20)
    assert outcome == "Out of Bounds"
    assert message == "⚠️ Guess must be between 1 and 20!"


def test_easy_difficulty_range():
    """Test that Easy difficulty returns range 1 to 20"""
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_normal_difficulty_range():
    """Test that Normal difficulty returns range 1 to 100"""
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100


def test_hard_difficulty_range():
    """Test that Hard difficulty returns range 1 to 50"""
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

