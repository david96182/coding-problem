from datetime import datetime


class Incident:
    def __init__(self, status, description, date_open, date_solved=None):
        self._status = status if status else 'open'
        self._description = description

        if date_open:
            if isinstance(date_open, datetime):
                self._date_open = date_open
            else:
                self._date_open = datetime.strptime(date_open, '%Y-%m-%d %H:%M:%S')
        else:
            self._date_open = datetime.now()

        if date_solved:
            if isinstance(date_solved, datetime):
                self._date_solved = date_solved
            else:
                self._date_solved = datetime.strptime(date_solved, '%Y-%m-%d %H:%M:%S')
        else:
            self._date_solved = None

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_date_open(self):
        return self._date_open

    def set_date_open(self, date_open):
        self._date_open = date_open

    def get_date_solved(self):
        return self._date_solved

    def set_date_solved(self, date_solved):
        self._date_solved = date_solved

    def __str__(self):
        return f'{self._status} - {self._description} - {self._date_open} - {self._date_solved}'
