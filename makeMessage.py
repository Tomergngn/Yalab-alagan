def main(day, hour, hug, gender) -> str:
    gender = ("" if gender == "Male" else "י")
    if day == "ראשון":
        day = "ביום ראשון"
    if hug == "Chess":
        return f"היי מה שלומך?\nהאם תגיע{gender} לשיעור מחר?"
    tmp = f"היי מה שלומך?\nהאם תגיע{gender} {day} לשיעור"
    if hug == "BJJ" or hug == "BJJ Morning":
        tmp += f" בשעה {hour}"
    return tmp + "?"