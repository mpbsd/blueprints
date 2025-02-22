from datetime import date, timedelta

from pkgs.cron import blueprints
from pkgs.lazy import dates


class Blueprint:

    MONTH = {
        "01": "Jan",
        "02": "Fev",
        "03": "Mar",
        "04": "Abr",
        "05": "Mai",
        "06": "Jun",
        "07": "Jul",
        "08": "Ago",
        "09": "Set",
        "10": "Out",
        "11": "Nov",
        "12": "Dez",
    }

    WEEKD = {
        "01": "Se",
        "02": "Te",
        "03": "Qa",
        "04": "Qi",
        "05": "Sx",
        "06": "Sa",
        "07": "Do",
    }

    SCHDL = {
        "24": {2: timedelta(days=2), 4: timedelta(days=5)},
        "35": {3: timedelta(days=2), 5: timedelta(days=5)},
        "46": {4: timedelta(days=2), 6: timedelta(days=5)},
        "246": {
            2: timedelta(days=2),
            4: timedelta(days=2),
            6: timedelta(days=3),
        },
    }

    def __init__(self, opening, code, shift):
        self.opening = date.fromisoformat(opening)
        self.code = code
        self.schedule = self.SCHDL[shift]

    def lazy(self):
        return [date.fromisoformat(x) for x in dates]

    def cron(self):
        cron = []
        date = self.opening
        if date.isoweekday() not in self.schedule.keys():
            while date.isoweekday() not in self.schedule.keys():
                date += timedelta(days=1)
        for bp in blueprints[self.code]["cron"]:
            CONTENT = bp[0]
            HOWMANY = bp[1] // 2
            if date in self.lazy():
                while date in self.lazy():
                    date += self.schedule[date.isoweekday()]
            cron.append((date, CONTENT, HOWMANY * 2))
            while HOWMANY > 0:
                date += self.schedule[date.isoweekday()]
                HOWMANY -= 1
        return cron

    def show(self):
        show = []
        for bp in self.cron():
            date, content, howmany = bp
            w = self.WEEKD[f"{date.isoweekday():02d}"]
            y = date.year
            m = self.MONTH[f"{date.month:02d}"]
            d = date.day
            s = "aulas" if howmany > 1 else "aula"
            r = f"\\item[{w} {d:02d}/{m}/{y}] {content} ({howmany} {s})"
            show.append(r)
        return show

    def save(self):
        with open(f"brew/{self.code}.tex", "w") as tex_file:
            for bp in self.show():
                print(bp, file=tex_file)

    def __repr__(self):
        return f"{self.code}: {blueprints[self.code]['name']}"
