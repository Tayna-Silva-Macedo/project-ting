import sys

from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def is_new_file(path_file, instance):
    for index in range(len(instance)):
        file = instance.search(index)
        if file["nome_do_arquivo"] == path_file:
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


def remove(instance: Queue):
    if instance.is_empty():
        return sys.stdout.write("Não há elementos\n")

    file_removed = instance.dequeue()
    file_name = file_removed["nome_do_arquivo"]

    return sys.stdout.write(f"Arquivo {file_name} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
    except IndexError:
        return sys.stderr.write("Posição inválida")

    return sys.stdout.write(f"{file}")
