import textwrap

def feedbackReview(feedback, size):
    return textwrap.wrap(feedback,size)


feedback = "I'm not sure how your service is supposed to work, is there some readme or something?"
size = 12

print(feedbackReview(feedback,size))

# не совсем верное, но стоит доработать
import re
def feedbackReview2(feedback, size):
    return re.findall(r".{0,%d} "%size, feedback)

print(feedbackReview2(feedback,size))