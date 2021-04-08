from calendar import HTMLCalendar, SUNDAY

class Calendar(HTMLCalendar):

    def __init__(self, event_provider):
        self._event_provider = event_provider
        super().__init__(SUNDAY) # display week starting on sunday

    def formatday(self, day, weekday, month, year):
        """
        Return a day as a table cell.
        """
        if day == 0:
            return f'<td class="{self.cssclass_noday}">&nbsp;</td>' # day outside month
        else:
            cssclass = "weekday" if 0 <= weekday <= 4 else "weekend"
            cell = f'<td class="{cssclass}">{day}<div class="scrollable">'
            events = self._event_provider.get_events(day, month, year)
            if events is not None:
                cell += '<ul>'
                for event in events:
                    data = f'data-title="{event.title}" data-content="{event.description}" '
                    data += f'data-time="{event.get_time_string()}" data-location="{event.location}" '
                    data += f'data-link="{event.link}" '
                    cell += f'<li class="event" data-toggle="modal" data-target="#eventModal" {data}>'
                    cell += f'<strong>{event.calendar_display_time()}</strong> {event.title}</li>'
                    if len(events) > 1:
                        cell += '<hr class="solid">'
                cell += '</ul>'
            cell += '</div></td>'
            return cell

    def formatweek(self, theweek, month, year):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd, month, year) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s

    def formatweekheader(self):
        """
        Return a header for a week as a table row.
        """
        s = ''.join(self.formatweekday(i) for i in self.iterweekdays())
        return '<tr>%s</tr>' % s

    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """
        month = ''
        month += '<table border="0" cellpadding="0" cellspacing="0" class="month">'
        month += '\n'
        month += self.formatmonthname(theyear, themonth, withyear=withyear)
        month += '\n'
        month += self.formatweekheader()
        month += '\n'
        for week in self.monthdays2calendar(theyear, themonth):
            month += self.formatweek(week, themonth, theyear)
            month += '\n'
        month += '</table>'
        month += '\n'
        return month