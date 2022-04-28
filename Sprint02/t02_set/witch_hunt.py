def witch_hunt(susp_sets, inno_sets):
    if not susp_sets and not inno_sets:
        return set()
    elif not susp_sets:
        return set()
    elif not inno_sets:
        return set.intersection(*susp_sets)
    else:
        witch = set.intersection(*susp_sets)
        return witch.difference(*inno_sets)
