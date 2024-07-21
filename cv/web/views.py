from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.utils.translation import activate



# A database storage for this sounds perfect, but
# requires additional service (additional payment)
# so I'm just defining these inline.
CONTENT = [
    {
        "what": _("Born"),
        "when": _("30 March 1990"),
        "where": _("Oriahovo"),
        "link": "https://www.oriahovo.bg/",
        "category": "personal"
    },
    {
        "what": _("Primary Education"),
        "when": "2004",
        "where": _("OU \"N. Y. Vaptsarov\"<br/>Selanovtsi"),
        "link": "https://ouvaptsarov-selanovtsi.info/",
        "category": "education"
    },
    {
        "what": _("The only one with 6.00 at the high school candidate exam in Mathematics for the administrative area"),
        "when": "2004",
        "where": _("OU \"N. Y. Vaptsarov\"<br/>Selanovtsi"),
        "link": "https://ouvaptsarov-selanovtsi.info/",
        "category": "education"
    },
    {
        "what": _("Third place at a national mathematics competition"),
        "when": "2005",
        "where": _("Natural Science and Mathematical School \"Akademik Ivan Tsenov\"<br/>Vratza"),
        "link": "https://pmg-vratsa.org/",
        "category": "education"
    },
    {
        "what": _("Secondary education"),
        "when": "2009",
        "where": _("Natural Science and Mathematical School \"Akademik Ivan Tsenov\"<br/>Vratza"),
        "link": "https://pmg-vratsa.org/",
        "category": "education"
    },
    {
        "what": _("Tertiary education<br/> (dropped)<br/>/Software engineering/"),
        "when": "2009-2011",
        "where": _("Faculty of mathematics and Informatics, Sofia University \"St. Kliment Ohridski\""),
        "link": "https://www.fmi.uni-sofia.bg/",
        "category": "education"
    },
    {
        "what": _("Developer of marketing research surveys<br/><i class='small'>(Python, HTML, CSS, JavaScript, Flash)</i>"),
        "when": "2010-2020",
        "where": _("\"Bright Marketing Research\"<br/>Sofia"),
        "link": "https://bright-research.com/",
        "category": "professional"
    },
    {
        "what": _("Awarded with an MVP prize by the company"),
        "when": "2012",
        "where": _("\"Bright Marketing Research\"<br/>Sofia"),
        "link": "https://bright-research.com/",
        "category": "professional"
    },
    {
        "what": _("Becomes a proud father of Victoria"),
        "when": "2018",
        "where": _("\"Mother's Home\" Hospital<br/>Sofia"),
        "link": "https://maichindom.com/",
        "category": "personal"
    },
    {
        "what": _("Senior Python Developer<br/>&<br/>Tech Lead<br/><i class='small'>(Python, Django, CI/CD with Jenkins and GitHub Actions)</i>"),
        "when": "2020+",
        "where": _("\"Strypes\"<br/>Sofia"),
        "link": "https://strypes.eu/",
        "category": "professional"
    },
    {
        "what": _("Lecture for dev.bg"),
        "when": "2022",
        "where": "#TODO or not #TODO",
        "link": "https://dev.bg/event/todo-or-not-todo-should-python-enhancement-proposal-350-have-been-accepted/",
        "category": "professional"
    },
    {
        "what": _("Python Lecturer"),
        "when": "2022+",
        "where": _("Python course at FMI"),
        "link": "https://py-fmi.org/",
        "category": "professional"
    },
    {
        "what": _("Creates the website for the Python course at FMI<br/><i class='small'>(Python, Django, jQuery, Bootstrap, PostgreSQL, Celery, Docker)</i>"),
        "when": "2023",
        "where": _("The project at GitHub"),
        "link": "https://github.com/gvkunchev/shrubbery",
        "category": "professional"
    },
    {
        "what": _("Creates the current CV"),
        "when": "2024",
        "where": _("The project at GitHub"),
        "link": "https://github.com/gvkunchev/web_cv",
        "category": "personal"
    },
]

# Not appropriate translation approach for a fully-fledged project.
# This is simple one-pager so keep it simple and save time to spend with the family

def index_bg(request):
    """Index bg view."""
    activate('bg')
    return render(request, 'index.html', {'content': CONTENT})

def index_en(request):
    """Index en view."""
    activate('en-us')
    return render(request, 'index.html', {'content': CONTENT})
