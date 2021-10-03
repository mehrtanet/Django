# from django.core.exceptions import ValidationError
from django.contrib import admin


#Post model(state field)
Accepted = 1
Pending = 2
Rejected = 0

POST_STATUS_TYPES = [
    (Accepted, 'تایید'),
    (Pending, 'در حال بررسی'),
    (Rejected, 'عدم تایید'),
]


#Post model(category field)
Scintific = 2
Educational = 1
news = 0

POST_CATEGORY_TYPES = [
    (Scintific, 'علمی'),
    (Educational, 'آموزشی  '),
    (news, 'خبری '),
]


def post_image_path(instance, filename):
    return 'post-image/%s.%s' %(instance.title , filename.split(".")[-1])