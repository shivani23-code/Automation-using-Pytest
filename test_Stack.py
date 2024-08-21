import pytest
from StackDetails import Stack

@pytest.fixture
def stack():
    return Stack()

def test_push(stack):
    stack.push(1)
    assert stack.size() == 1
    assert stack.peek() == 1

def test_pop(stack):
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.size() == 1

def test_pop_empty(stack):
    with pytest.raises(IndexError):
        stack.pop()

def test_peek(stack):
    stack.push(1)
    assert stack.peek() == 1

def test_peek_empty(stack):
    with pytest.raises(IndexError):
        stack.peek()

def test_is_empty(stack):
    assert stack.is_empty() is True
    stack.push(1)
    assert stack.is_empty() is False
