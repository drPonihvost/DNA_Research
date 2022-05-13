from .models import *

EXPORT_FILE_HEADER = [
    'Инициалы, Фамилия', 'должность', 'Орган назначивший',
    'Фамилия', 'Имя', 'Отчество', 'Дата рождения',	'место рождения',
    '№ дела (с указанием категории: у/д, РД, КУСП и т.д.)',	'Состав преступления',
    'Статья УК', 'Степень родства (заполняется для родственников разыскиваемых)'
]

def get_all_research():
    return Research.objects.all()


def get_research_by_id(research_id):
    return Research.objects.get(pk=research_id)


def check_related(research_id):
    return Research.objects.get(pk=research_id).relative_search


def get_person_by_research_id(research_id):
    return Person.objects.filter(research_id=research_id)


def get_all_persons():
    return Person.objects.all()


def prepare_line(line):
    return line[0].upper() + line[1::] if line else ''


def research_export(researches_id: list):
    file_name = 'export_file.txt'
    with open(file_name, 'w', encoding="windows-1251") as file:
        file.write('\t'.join(EXPORT_FILE_HEADER) + '\n')
        for research_id in researches_id:
            research = get_research_by_id(research_id)
            persons = get_person_by_research_id(research_id)
            for person in persons:
                export_data = [
                    f'{research.initiator_name[0].upper()}.{research.initiator_patronymic[0].upper()}. {prepare_line(research.initiator_surname)}',
                    prepare_line(research.initiator_post),
                    prepare_line(research.initiator_department),
                    prepare_line(person.surname),
                    prepare_line(person.name),
                    prepare_line(person.patronymic),
                    str(person.birthday),
                    person.birthplace,
                    research.event_number,
                    prepare_line(research.plot),
                    research.article if research.article else '',
                    prepare_line(person.relation)
                ]
                file.write('\t'.join(export_data) + '\n')
    return file_name
