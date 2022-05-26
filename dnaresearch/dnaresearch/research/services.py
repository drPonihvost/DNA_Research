from .models import *


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


def output_capital(line):
    return line[0].upper() + line[1::] if line else ''


class ExportFile:
    EXPORT_FILE_HEADER = [
        'Инициалы, Фамилия', 'должность', 'Орган назначивший',
        'Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'место рождения',
        '№ дела (с указанием категории: у/д, РД, КУСП и т.д.)', 'Состав преступления',
        'Статья УК', 'Степень родства (заполняется для родственников разыскиваемых)'
    ]
    FILE_NAME = 'export_file.txt'
    ENCODING = 'windows-1251'
    SEPARATOR = '\t'
    END = '\n'

    def __init__(self, researches_id: list) -> None:
        self.researches_id = researches_id

    def write_header(self, file):
        file.write(self.SEPARATOR.join(self.EXPORT_FILE_HEADER) + self.END)

    @staticmethod
    def output_capital(string: str) -> str:
        return string[0].upper() + string[1::] if string else ''

    def write_data(self, file):
        for research_id in self.researches_id:
            research = get_research_by_id(research_id)
            persons = get_person_by_research_id(research_id)
            for person in persons:
                export_data = [
                    f'{research.initiator_name[0].upper()}.{research.initiator_patronymic[0].upper()}. {output_capital(research.initiator_surname)}',
                    output_capital(research.initiator_post),
                    output_capital(research.initiator_department),
                    output_capital(person.surname),
                    output_capital(person.name),
                    output_capital(person.patronymic),
                    str(person.birthday),
                    person.birthplace,
                    research.event_number,
                    output_capital(research.plot),
                    research.article if research.article else '',
                    output_capital(person.relation)
                ]
                file.write(self.SEPARATOR.join(export_data) + self.END)

    def create_txt(self) -> None:
        with open(self.FILE_NAME, 'w', encoding=self.ENCODING) as file:
            self.write_header(file)
            self.write_data(file)
