import pytest

# импортируем класс HobbitsPriorityStatus из файла miles.py
from miles import HobbitsPriorityStatus

test_data = [
    ('Фродо', 'Platinum'),
    ('Сэм', 'Gold'),
    ('Мэри', 'Silver'),
    ('Пиппин', 'Silver'),
]

class TestHobbitsPriorityStatus:

    
    @pytest.mark.parametrize('hobbit, priority_status', test_data)
    def test_priority_status(self, hobbit, priority_status):
        assert HobbitsPriorityStatus().get_status(hobbit) == priority_status
