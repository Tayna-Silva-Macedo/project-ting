import pytest

from ting_file_management.priority_queue import PriorityQueue


@pytest.fixture
def mock_big_file():
    return {
        "nome_do_arquivo": "big_file.txt",
        "qtd_linhas": 40,
        "linhas_do_arquivo": ["big file text"],
    }


@pytest.fixture
def mock_medium_file():
    return {
        "nome_do_arquivo": "medium_file.txt",
        "qtd_linhas": 10,
        "linhas_do_arquivo": ["medium file text"],
    }


@pytest.fixture
def mock_little_file():
    return {
        "nome_do_arquivo": "little_file.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["little file text"],
    }


def test_basic_priority_queueing(
    mock_big_file, mock_medium_file, mock_little_file
):
    priority_queue = PriorityQueue()

    priority_queue.enqueue(mock_big_file)
    assert len(priority_queue) == 1

    priority_queue.enqueue(mock_medium_file)
    assert len(priority_queue) == 2

    priority_queue.enqueue(mock_little_file)
    assert len(priority_queue) == 3

    file_index_zero = priority_queue.search(0)
    assert file_index_zero == mock_little_file

    file_index_one = priority_queue.search(1)
    assert file_index_one == mock_big_file

    file_index_two = priority_queue.search(2)
    assert file_index_two == mock_medium_file

    with pytest.raises(IndexError):
        priority_queue.search(100)

    file_zero_removed = priority_queue.dequeue()
    assert file_zero_removed == mock_little_file
    assert len(priority_queue) == 2

    file_one_removed = priority_queue.dequeue()
    assert file_one_removed == mock_big_file
    assert len(priority_queue) == 1

    file_two_removed = priority_queue.dequeue()
    assert file_two_removed == mock_medium_file
    assert len(priority_queue) == 0
