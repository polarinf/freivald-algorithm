import numpy as np
import pytest
from freivald import Freivald


@pytest.fixture()
def frv():
    return Freivald(10)


def test_verify_freivald(frv):
    # Given
    file_path = '/Users/samsung/Documents/repos/algorithm-tests/tests/freivald_input.txt'

    # When
    result = frv.verify_freivald(file_path)

    # Then
    print(result)


def test_compute_freivald(frv):
    # Given
    file_path = '/Users/samsung/Documents/repos/algorithm-tests/tests/freivald_input.txt'

    # When
    m1 = [[1, 1], [1, 1]]
    m2 = [[2, 2], [2, 2]]
    m3 = [[4, 4], [4, 4]]
    result = frv.compute_freivald(m1, m2, m3, file_path)

    # Then
    assert isinstance(result, bool)
    print(result)


def test_get_matrix_dim(frv):
    # Given
    file_path = '/Users/samsung/Documents/repos/algorithm-tests/tests/freivald_input.txt'

    # When
    matrix_size = frv.get_matrix_dim(file_path)
    with open(f'{file_path}', 'r') as file:
        first_line = int(file.readline().split('\n')[0])

    # Then
    assert matrix_size == first_line
    print(matrix_size)


def test_get_matrix(frv):
    # Given
    file_path = '/Users/samsung/Documents/repos/algorithm-tests/tests/freivald_input.txt'

    # When
    matrix_dict = frv.get_matrix(file_path)

    # Then
    assert isinstance(matrix_dict, dict)
    assert len(matrix_dict) == 3


def test_shape_matrix(frv):
    # Given
    file_path = '/Users/samsung/Documents/repos/algorithm-tests/tests/freivald_input.txt'
    entries = []
    for i in (frv.clean_contents(file_path)):
        temp = frv.str_to_int(i)
        entries.append(temp)

    # When
    shaped_matrix_list = []
    for i in entries[1:]:
        temp = frv.shape_matrix(i, file_path)
        shaped_matrix_list.append(temp)

    # Then
    for matrix in shaped_matrix_list:
        assert isinstance(matrix, np.matrix)
        assert matrix.ndim == frv.get_matrix_dim(file_path)


def test_read_txt(frv):
    # Given
    file_path = '/Users/samsung/Documents/repos/algorithm-tests/tests/freivald_input.txt'

    # When
    result = frv.read_txt(file_path)

    # Then
    assert len(result) == 4
    for item in result:
        assert isinstance(item, str)
    print(result)


def test_clean_contents(frv):
    # Given
    file_path = '/Users/samsung/Documents/repos/algorithm-tests/tests/freivald_input.txt'

    # When
    result = frv.clean_contents(file_path)

    # Then
    assert len(result) == 4
    for i in result:
        for j in i:
            assert isinstance(j, str)
            assert '\n' not in j
    print(result)


def test_get_random_vector(frv):
    # Given
    file_path = '/Users/samsung/Documents/repos/algorithm-tests/tests/freivald_input.txt'

    # When
    rv = frv.get_random_vector(file_path)

    # Then
    assert len(rv) == frv.get_matrix_dim(file_path)
    assert isinstance(rv, np.ndarray)
    print(rv)


def test_multiply_matrix(frv):
    # Given
    m1 = [[1, 1], [1, 1]]
    m2 = [[2, 2], [2, 2]]
    m1m2 = [[4, 4], [4, 4]]

    # When
    mul_matrix = frv.multiply_matrix(m1, m2)

    # Then
    assert np.all(mul_matrix) == np.all(m1m2)
    print(mul_matrix)


def test_str_to_int(frv):
    # Given
    str_list = ['1', '2', '3', '4']

    # When
    result = frv.str_to_int(str_list)

    # Then
    for item in result:
        assert isinstance(item, int)
    assert len(result) == len(str_list)
    print(result)


def test_clean_text(frv):
    # Given
    raw_text = '\n'

    # When
    result = frv.clean_text(raw_text)

    # Then
    assert '\n' not in result


def test_split_text(frv):
    # Given
    raw_text = 'a b'

    # When
    result = frv.split_text(raw_text)

    # Then
    assert isinstance(result, list)
    assert len(result) == 2
    assert 'a', 'b' in result
