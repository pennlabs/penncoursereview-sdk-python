"""Get a list of average scores for each professor in a department."""
import sys
from collections import defaultdict

import penncoursereview as pcr


def prof_scores(dept):
    professor_scores = defaultdict(list)
    dept = pcr.Department(dept)
    for review in dept.reviews.values:
        instructor = review.instructor
        rating = review.ratings.rInstructorQuality
        professor_scores[instructor.name].append(float(rating))
    return professor_scores


def averages(dept):
    professor_scores = prof_scores(dept)
    for prof, scores in professor_scores.iteritems():
        score = sum(scores) / len(scores)
        yield prof, score


def main(dept):
    for prof, avg in sorted(averages(dept), key=lambda x: x[1]):
        print "%s %.2f" % (prof, avg)


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print "usage: scores.py <department>"
    else:
        main(sys.argv[1])
