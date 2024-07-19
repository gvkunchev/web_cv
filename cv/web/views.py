from django.shortcuts import render


# A database storage for this sounds perfect, but
# requires additional service (additional payment)
# so I'm just defining these inline.
CONTENT = [
    {
        "what": "Роден",
        "when": "30 Март 1990",
        "where": "гр. Оряхово",
        "link": "https://www.oriahovo.bg/",
        "category": "personal"
    },
    {
        "what": "Основно образование",
        "when": "2004",
        "where": "ОУ \"Н. Й. Вапцаров\" Селановци",
        "link": "https://ouvaptsarov-selanovtsi.info/",
        "category": "education"
    },
    {
        "what": "Единственият с резултат 6.00 на кандидат-гимназисткия изпити по математика за областта",
        "when": "2004",
        "where": "ОУ \"Н. Й. Вапцаров\" Селановци",
        "link": "https://ouvaptsarov-selanovtsi.info/",
        "category": "education"
    },
    {
        "what": "Трето място на национално състезание по математика",
        "when": "2005",
        "where": "ПМГ \"Академик Иван Ценов\" гр.Враца",
        "link": "https://pmg-vratsa.org/",
        "category": "education"
    },
    {
        "what": "Средно образование",
        "when": "2009",
        "where": "ПМГ \"Академик Иван Ценов\" гр.Враца",
        "link": "https://pmg-vratsa.org/",
        "category": "education"
    },
    {
        "what": "Висше образование<br/> (прекъснал)<br/>/Софтуерно инженерство/",
        "when": "2009-2011",
        "where": "ФМИ kъм<br/> СУ \"Св. Климент Охридски\"<br/> София",
        "link": "https://www.fmi.uni-sofia.bg/",
        "category": "education"
    },
    {
        "what": "Програмист маркетингови проучвания<br/><i class='small'>(Python, HTML, CSS, JavaScript, Flash)</i>",
        "when": "2010-2020",
        "where": "\"Брайт Маркетинг Рисърч\" София",
        "link": "https://bright-research.com/",
        "category": "professional"
    },
    {
        "what": "Получава приз MVP на фирмата",
        "when": "2005",
        "where": "\"Брайт Маркетинг Рисърч\" София",
        "link": "https://bright-research.com/",
        "category": "professional"
    },
    {
        "what": "Става горд баща на Виктория",
        "when": "2018",
        "where": "Болница \"Майчин дом\" София",
        "link": "https://maichindom.com/",
        "category": "personal"
    },
    {
        "what": "Senior Python Developer<br/>&<br/>Tech Lead<br/><i class='small'>(Python, Django, CI/CD with Jenkins and GitHub Actions)</i>",
        "when": "2020+",
        "where": "\"Страйпс\" София",
        "link": "https://strypes.eu/",
        "category": "professional"
    },
    {
        "what": "Лектор по Python",
        "when": "2022+",
        "where": "Курс по Python във ФМИ",
        "link": "https://py-fmi.org/",
        "category": "professional"
    },
    {
        "what": "Създава сайтът за курса по Python във ФМИ<br/><i class='small'>(Python, Django, jQuery, Bootstrap, PostgreSQL, Celery, Docker)</i>",
        "when": "2023",
        "where": "Проектът в GitHub",
        "link": "https://github.com/gvkunchev/shrubbery",
        "category": "professional"
    },
    {
        "what": "Създава текущото CV",
        "when": "2024",
        "where": "Проектът в GitHub",
        "link": "#",
        "category": "personal"
    },
]


def index(request):
    """Index view."""
    return render(request, 'index.html', {'content': CONTENT})
