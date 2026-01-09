def text_to_gloss(text):
    words = text.split()
    gloss = []

    for w in words:
        if w in ["నేను", "నాకు"]:
            gloss.append("I")
        elif "పాఠశాల" in w:
            gloss.append("SCHOOL")
        elif "వెళ్తు" in w:
            gloss.append("GO")

    return gloss
