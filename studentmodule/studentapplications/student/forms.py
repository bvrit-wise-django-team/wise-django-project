from django.forms import ModelForm
from student.models import StudentContactDetails
class ViewForm (ModelForm):
	class Meta :
		model = StudentContactDetails
		fields = '__all__'

