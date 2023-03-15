class New(object):
    title = ""
    score = ""
    date = ""
    comments = ""

    def __new__(cls, title, subtext):
        cls.title = title.a.text
        score = subtext.find("span", attrs={"class": "score"})

        if score is not None:
            cls.score = score.text
        else:
            cls.score = "0 points"

        cls.date = subtext.find("span", attrs={"class": "age"})["title"]
        cls.comments = subtext.findAll("a")[-1].text

        return cls

