def oxford_comma(items):
    if len(items) == 1:
        return ''.join(items)
    if len(items) == 2:
        return ' and '.join(items)
    if len(items) >= 3:
        last = items.pop()
        first = ', '.join(items)
        return first + ', and ' + last
