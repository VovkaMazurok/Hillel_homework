class GroupOverflowException(Exception):
    def __str__(self):
        return "Максимальна кількість студентів: 10"