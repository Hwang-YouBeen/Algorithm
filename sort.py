from typing import List, Tuple

def sort_list(seq, inplace=True, ascending=True) -> List[object]:
    if inplace:
        seq.sort(reverse=not ascending)
        return seq
    else:
        sorted_seq = seq[:]
        sorted_seq.sort(reverse=not ascending)
        return sorted_seq
    pass

def sort_objects(seq, key, inplace=True, ascending=True) -> List[object]:
    if inplace:
        seq.sort(key=key, reverse=not ascending)
        return seq
    else:
        sorted_seq = seq[:]
        sorted_seq.sort(key=key, reverse=not ascending)
        return sorted_seq
    pass

def sort_dict_by_key(kv, ascending=True) -> List[Tuple[object, object]]:
    sorted_items = sorted(kv.items(), key=lambda x: x[0], reverse=not ascending)
    return sorted_items
    pass

def sort_dict_by_val(kv, ascending=True) -> List[Tuple[object, object]]:
    sorted_items = sorted(kv.items(), key=lambda x: x[1], reverse=not ascending)
    return sorted_items
    pass