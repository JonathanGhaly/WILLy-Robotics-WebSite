from datetime import date
from courses.models import Course,Competition
import courses 
def ageChecker(date2,coursePK):
    thisDate = date.today()
    thisYear = int(thisDate.strftime("%Y"))
    course = Course.objects.get(id=coursePK)
    year =int(date2.strftime("%Y"))
    if thisYear-year >= int(course.min_age) and thisYear-year <=  int(course.max_age):
        return True
    return False
def ageCheckerComp(date2,compPK):
    thisDate = date.today()
    thisYear = int(thisDate.strftime("%Y"))
    course = Competition.objects.get(id=compPK)
    year =int(date2.strftime("%Y"))
    if thisYear-year >= int(course.min_age) and thisYear-year <=  int(course.max_age):
        return True
    return False
