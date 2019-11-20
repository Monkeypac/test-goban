from goban import Goban

# fmt: off

def test_white_is_taken_when_surrounded_by_black():
    goban = Goban([
        '.#.',
        '#o#',
        '.#.',
    ])

    assert goban.is_taken(1, 1) is True


def test_white_is_not_taken_when_it_has_a_liberty():
    goban = Goban([
        '...',
        '#o#',
        '.#.',
    ])

    assert goban.is_taken(1, 1) is False


def test_black_shape_is_taken_when_surrounded():
    goban = Goban([
        'oo.',
        '##o',
        'o#o',
        '.o.',
    ])

    assert goban.is_taken(0, 1) is True
    assert goban.is_taken(1, 1) is True
    assert goban.is_taken(1, 2) is True


def test_black_shape_is_not_taken_when_it_has_a_liberty():
    goban = Goban([
        'oo.',
        '##.',
        'o#o',
        '.o.',
    ])

    assert goban.is_taken(0, 1) is False
    assert goban.is_taken(1, 1) is False
    assert goban.is_taken(1, 2) is False


def test_square_shape_is_taken():
    goban = Goban([
        'oo.',
        '##o',
        '##o',
        'oo.',
    ])

    assert goban.is_taken(0, 1) is True
    assert goban.is_taken(0, 2) is True
    assert goban.is_taken(1, 1) is True
    assert goban.is_taken(1, 2) is True

def test_full_shape_is_taken():
    goban = Goban([
        '###',
        '###',
        '###',
    ])

    assert goban.is_taken(0, 0) is True
    assert goban.is_taken(0, 1) is True
    assert goban.is_taken(0, 2) is True
    assert goban.is_taken(1, 0) is True
    assert goban.is_taken(1, 1) is True
    assert goban.is_taken(1, 2) is True
    assert goban.is_taken(2, 0) is True
    assert goban.is_taken(2, 1) is True
    assert goban.is_taken(2, 2) is True

def test_two_shapes_one_taken_one_not():
    goban = Goban([
        '#o.',
        'o#.',
        '...',
    ])

    assert goban.is_taken(0, 0) is True
    assert goban.is_taken(1, 1) is False

def test_circle():
    goban = Goban([
        '###',
        '#.#',
        '###',
    ])

    assert goban.is_taken(0, 0) is False
    assert goban.is_taken(1, 1) is False

def test_circle_with_whites():
    goban = Goban([
        'ooooo',
        'o###o',
        'o#.#o',
        'o###o',
        'ooooo'
    ])

    assert goban.is_taken(0, 0) is True
    assert goban.is_taken(1, 1) is False
    assert goban.is_taken(2, 2) is False

def test_empty_not_taken():
    goban = Goban([
        '.'
    ])

    assert goban.is_taken(0, 0) is False

def test_diagonals_do_not_count():
    goban = Goban([
        'o.o',
        '.x.',
        'o.o',
    ])

    assert goban.is_taken(1, 1) is False
