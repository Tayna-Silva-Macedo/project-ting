import sys

from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def is_new_file(path_file, instance):
    for index in range(len(instance)):
        element = instance.search(index)
        if element["nome_do_arquivo"] == path_file:
            return False

    return True


def process(path_file, instance):
    if is_new_file(path_file, instance):
        content = txt_importer(path_file)

        file_info = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(content),
            "linhas_do_arquivo": content,
        }

        instance.enqueue(file_info)
        return sys.stdout.write(f"{file_info}\n")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


process("statics/arquivo_teste.txt", Queue())
