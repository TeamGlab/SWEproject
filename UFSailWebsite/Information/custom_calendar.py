from calendar import HTMLCalendar

class Calendar(HTMLCalendar):

    def formatday(self, day, weekday):
        """
        Return a day as a table cell.
        """
        if day == 0:
            # day outside month
            return '<td class="%s">&nbsp;</td>' % self.cssclass_noday
        else:
            cssclass = "weekday" if 0 <= weekday <= 4 else "weekend"
            return '<td class="%s">%d</td>' % (cssclass, day)

    def formatweek(self, theweek):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd) for (d, wd) in theweek)
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
            month += self.formatweek(week)
            month += '\n'
        month += '</table>'
        month += '\n'
        return month