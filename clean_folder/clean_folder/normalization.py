


def normalize(basename, file_extention): # переклад назви файлів на латиницю
    cyrylic_symbols = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    latin_symbols = ("a", "b", "v", "h", "g", "d", "e", "ye", "j", "z", "y", "i", "yi", "y", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "yu", "ya")
    transl = {}
    for а, a in zip(cyrylic_symbols, latin_symbols):
        transl[ord(а)] = a
        transl[ord(а.upper())] = a.upper()
        transl_name = basename.translate(transl)
    upd_name = ""
    for l in transl_name: #заміна різних символів на нижнє підкресленя
        if l.isdigit() != True and l.isalpha() !=True:
            upd_name += "_"
        else:
            upd_name += l
    the_name = upd_name + file_extention #об'єдную нормалізовану назву з суфіксом (розширення файлу)
    return the_name


def normalize_noext(basename): # переклад назви файлів на латиницю
    cyrylic_symbols = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    latin_symbols = ("a", "b", "v", "h", "g", "d", "e", "ye", "j", "z", "y", "i", "yi", "y", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "yu", "ya")
    transl = {}
    for а, a in zip(cyrylic_symbols, latin_symbols):
        transl[ord(а)] = a
        transl[ord(а.upper())] = a.upper()
        transl_name = basename.translate(transl)
    upd_name = ""
    for l in transl_name: #заміна різних символів на нижнє підкресленя
        if l.isdigit() != True and l.isalpha() !=True:
            upd_name += "_"
        else:
            upd_name += l
    return upd_name


