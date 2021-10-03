from django.core.exceptions import ValidationError
from django.contrib import admin


def profile_files_path(instance, filename):
    return 'cv-files/ %s.%s' %(instance.user , filename.split(".")[-1])


#Profile model(gender field)
Female = "خانم"
Male = "آقا"
Other = "دیگری"

Profile_Gender = [
    (Female, 'خانم'),
    (Male, 'آقا'),
    (Other, 'دیگری'),
]

#For Profile models(phone , n_code fields)
def check_is_digit(value) :
    if not value.isdigit():
        raise ValidationError("مقدار این فیلد باید عدد باشد ")


