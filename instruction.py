# This page would contain all The instruction for the operation we have performend in the project.

# Update the new model in the Polls app
# creating migration
# python manage.py makemigrations polls

# Applying migration
# (python manage.py migrate)

#Starting the Django Shell
# (python manage.py shell)

# shell commands

#importing Models
# >>> from polls.models import Question, Choice

# Displaying all the questions
# Question.objects.all()

# Creating objects in this case questions
# >>> from django.utils import timezone
# >>> q = Question(question_text="What's new?", pub_date=timezone.now())
# >>> q.save()

# Filtering the questions
# >>> Question.objects.filter(id=1)
# O/P<QuerySet [<Question: What's new?>]>
# >>> Question.objects.filter(question_text__startswith="What")
# O/P <QuerySet [<Question: What's new?>]>

# Updating the question
# >>> q = Question.objects.get(pk=1)
# >>> q.question_text = "What's up?"
# >>> q.save()

#Adding Choices to a Question:
# >>> q = Question.objects.get(pk=1)
# >>> q.choice_set.create(choice_text='Not much', votes=0)
# >>> q.choice_set.create(choice_text='The sky', votes=0)
# >>> q.choice_set.create(choice_text='Just hacking again', votes=0)

# retiving Choices
# >>> q.choice_set.all()
# O/P <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Registering Models in the admin interface
# python manage.py createsuperuser => start Server python manage.py runserver

# Adding the Question model to the admin interface by making changes in polls/admin.py

#filter the questions by pub_date
# >>> from django.utils import timezone
# >>> current_year = timezone.now().year
# >>> Question.objects.filter(pub_date__year=current_year)

#Ordering the questions by pub_date
# >>> Question.objects.order_by('-pub_date')

# using API to create and retrive objects
# >>> from polls.models import Question, Choice
# >>> from django.utils import timezone

# >>> q = Question.objects.create(question_text="What's your favorite programming language?", pub_date=timezone.now())
# >>> q.choice_set.create(choice_text='Python', votes=0)
# >>> q.choice_set.create(choice_text='JavaScript', votes=0)
# >>> q.choice_set.create(choice_text='Java', votes=0)

#retiving and displaying the Data
# >>> for choice in q.choice_set.all():
# ...     print(choice.choice_text)
# ...
# Python
# JavaScript
# Java


#updating Votes
# >>> c = q.choice_set.get(choice_text='Python')
# >>> c.votes += 1
# >>> c.save()

#deleting the object
# >>> c.delete()


