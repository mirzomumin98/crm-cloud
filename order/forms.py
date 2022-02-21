from django.forms import ModelForm

from crms.models import Order

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer']