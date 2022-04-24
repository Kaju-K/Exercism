def round_scores(student_scores):
    rounded_scores = []
    for score in student_scores:
        rounded_scores.append(round(score))
    return rounded_scores



def count_failed_students(student_scores):
    number_of_failed = 0
    for score in student_scores:
        if score <= 40:
            number_of_failed += 1
    return number_of_failed


def above_threshold(student_scores, threshold):
    scores_above_threshold = []
    for score in student_scores:
        if score >= threshold:
            scores_above_threshold.append(score)
    return scores_above_threshold


def letter_grades(highest):
    lower_thresholds = []
    interval = (highest - 40)//4
    for i in range(4):
        lower_thresholds.append(41+i*interval)
    return lower_thresholds

        


def student_ranking(student_scores, student_names):
    ranking = []
    for index, name in enumerate(student_names):
        ranking.append(f'{index + 1}. {name}: {student_scores[index]}')
    return ranking



def perfect_score(student_info):
    empty = []
    for grade in student_info:
        if grade[1] == 100:
            return grade
    return empty
