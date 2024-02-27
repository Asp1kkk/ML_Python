import datetime
import re
from typing import Optional


class RuDateParser:
    def parse_numeric(self, date: str) -> Optional[datetime.datetime]: 
        """ 
        Парсит даты в формате dd-mm-yyyy

        >>> RuDateParser().parse_numeric('01-12-2010')
        datetime.datetime(2010, 12, 1, 0, 0)

        >>> RuDateParser().parse_numeric('01/12/2010')

        >>> RuDateParser().parse_numeric('не дата')
        """

        if not isinstance(date, str):
            raise TypeError("No int in input")

        if not re.match('\d{2}-\d{2}-\d{4}', date): 
            return None
        date_splitted = date.split('-')
        day = int(date_splitted[0])
        month = int(date_splitted[1])
        year = int(date_splitted[2])
        try:
            return datetime.datetime(day=day, month=month, year=year)
        except:
            return None