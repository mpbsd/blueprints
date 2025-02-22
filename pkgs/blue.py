import os
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
        self.__open = date.fromisoformat(opening)
        self.__code = code
        self.__list = self.SCHDL[shift]
        self.cron = self.__cron()
        self.ltex = self.__ltex()
        self.save = self.__save()

    def __lazy(self):
        return [date.fromisoformat(x) for x in dates]

    def __cron(self):
        cron = []
        date = self.__open
        if date.isoweekday() not in self.__list.keys():
            while date.isoweekday() not in self.__list.keys():
                date += timedelta(days=1)
        for bp in blueprints[self.__code]["cron"]:
            CONTENT = bp[0]
            HOWMANY = bp[1] // 2
            if date in self.__lazy():
                while date in self.__lazy():
                    date += self.__list[date.isoweekday()]
            cron.append((date, CONTENT, HOWMANY * 2))
            while HOWMANY > 0:
                date += self.__list[date.isoweekday()]
                HOWMANY -= 1
        return cron

    def __ltex(self):
        show = []
        for bp in self.__cron():
            date, content, howmany = bp
            w = self.WEEKD[f"{date.isoweekday():02d}"]
            y = date.year
            m = self.MONTH[f"{date.month:02d}"]
            d = date.day
            s = "aulas" if howmany > 1 else "aula"
            r = f"\\item[{w} {d:02d}/{m}/{y}] {content} ({howmany} {s})"
            show.append(r)
        return show

    def __mdir(self):
        brew = os.path.expanduser(r"~/projects/blueprints/brew")
        if not os.path.isdir(brew):
            os.system(f"mkdir -p {brew}")

    def __save(self):
        self.__mdir()
        with open(f"brew/{self.__code}.tex", "w") as tex_file:
            for bp in self.__ltex():
                print(bp, file=tex_file)

    def __repr__(self):
        return f"{self.__code}: {blueprints[self.__code]['name']}"
