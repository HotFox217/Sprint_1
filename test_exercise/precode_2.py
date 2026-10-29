# импортируем класс HobbitsPriorityStatus из файла miles.py
from miles import HobbitsPriorityStatus


class TestHobbitsPriorityStatus:

    # допиши тест, который добавит в программу нового хоббита с именем Голлум,
    # начислит ему 50 миль и проверит его статус в системе
    def test_add_miles_and_check_status(self):
        hobbit = 'Голлум'
        hobbits_priority = HobbitsPriorityStatus()

        hobbits_priority.add_new_hobbit(hobbit)
        hobbits_priority.add_miles_to_hobbit(hobbit, 50)
        assert hobbits_priority.get_status(hobbit) == 'Classic'