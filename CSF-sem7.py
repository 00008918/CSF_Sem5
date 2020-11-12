csf = {
    "cw-weight" : 0.4,
    "cw-mark" : 90,
    "exam-weight" : 0.6,
    "exam-mark" : 75
}

def final():
    final_mark = csf.get("cw-weight", 0) * csf.get("cw-mark", 0) + csf.get("exam-weight", 0) * csf.get("exam-mark", 0)
    return final_mark

print(final())
