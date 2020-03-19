import pytest
from todo import Task

def test_set_is_done():
    task = Task(title='Sprzatanie', details='poodkurzac')
    task.set_is_done(True)
    assert task.is_done is True

def test_set_is_done_2():
    task = Task(title='Ugotować obiad', details='pokroic warzywa')
    task.set_is_done(True)
    assert task.is_done is True

    task.set_is_done(False)
    assert task.is_done is False

def test_str():
    task = Task(title='Sprzatanie', details='poodkurzac')
    result = task.__str__()
    expected = 'Sprzatanie\npoodkurzac\nis done: False'
    assert result == expected

def test_str_task_is_done():
    task = Task(title='Sprzatanie', details='poodkurzac')
    task.set_is_done(True)
    result = task.__str__()
    expected = 'Sprzatanie\npoodkurzac\nis done: True'
    assert result == expected