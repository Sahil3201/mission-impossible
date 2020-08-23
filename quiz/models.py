from django.db import models

# Create your models here.
# class Qna(models.Model):
# 	qid = models.IntegerField(unique=True)#[group:S-1, C-2][difficulty: E-1, M-2, H-3][q_no] - 5 digits

# 	q_no		= models.IntegerField(blank=True, null=True)
# 	question 	= models.CharField(max_length=1024)
# 	answer 		= models.CharField(max_length=255)
# 	difficulty	= models.CharField(max_length=1, choices=difficulty_choices, default='M') # H:Hard, M:Medium, E:Easy
# 	group 		= models.CharField(max_length=1, choices= group_choices) # S:School Students, C:College Students

# 	def __str__(self):
# 		# return self.group+'-'+self.difficulty+'-'+str(self.q_no)
# 		return str(self.qid)


from django.contrib.auth.models import AbstractUser
class Student(AbstractUser):
	name 			= models.CharField(max_length=255, blank=True, null=True)
	username		= models.IntegerField(unique=True)
	password 		= models.CharField(max_length=255)
	shown_at_time	= models.IntegerField(null=True,blank=True)
	
	ques_answered 	= models.IntegerField(blank=True, null=True, default=0) #Questions correctly answered
	attempt_for_q 	= models.SmallIntegerField(blank=True,null=True,default=5) #attempts remaining for the last attempted question
	# que_anwered = models.IntegerField(blank=True, null=True,default=0)
	# qna 	= models.ManyToManyField('Qna', blank=True, null=True)#,related_name='qna',on_delete=models.CASCADE)
	# score 	= models.IntegerField(default=0)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	def __str__(self):
		return str(self.username)

# class Answers(models.Model):
# 	student		= models.ForeignKey(Student, related_name='student', on_delete=models.CASCADE)
# 	qna 		= models.ForeignKey(Qna, related_name='qna', on_delete=models.CASCADE)
# 	correct		= models.BooleanField(null=True, blank=True)
# 	shown_at	= models.IntegerField()

# 	# class Meta:
# 	# 	order

# 	def __str__(self):
# 		return str(self.qna.qid)
# 		# return str(self.qna.qid)

# 	def __repr__(self):
# 		return str(self.qna.qid)
		# return str(self.student.name) + '-' + str(self.qna.difficulty) + str(self.qna.q_no)