from django import forms

from .models import Post,contact_model

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			"title",
			"subtitle",
			"content",
			"image",
			"draft",
			"publish",
		]
		widgets = {'title': forms.TextInput(
						attrs={
							'type':'text',
							'name':'title',
							'id':'title',
							'tabindex':'1',
							'class':'form-control',
							'placeholder':'Title',
							'value':'',
						}),
					'subtitle': forms.TextInput(
						attrs={
							'type':'text',
							'name':'subtitle',
							'tabindex':'1',
							'class':'form-control',
							'placeholder':'Subtitle',
							'value':'',

						}),
					'content': forms.Textarea(
						attrs={
							'type':'textarea',
							'name':'content',
							'id':'content',
							'tabindex':'2',
							'class':'content',
							'rows':'5',
						}),
					'publish': forms.TextInput(
						attrs={
							'type':'text',
							'name':'publish',
							'id':'publish',
							'tabindex':'2',
							'class':'form-control',
							'placeholder':'YYYY-MM-DD',
						}),
					}

class contactform(forms.ModelForm):
	class Meta:
		model = contact_model
		fields = [
			"name",
			"emailid",
			"contact_no",
			"message",
		]
		widgets = {'name': forms.TextInput(
						attrs={
							'type':'text',
							'class':'form-control',
							'placeholder':'Name',
							'id':'name',
							'data-validation-required-message':'Please enter your name.',
						}),
					'emailid': forms.TextInput(
						attrs={
							'type':'email',
							'class':'form-control',
							'placeholder':'Email Address',
							'id':'email',
							'data-validation-required-message':'Please enter your email address.',
						}),
					'contact_no': forms.TextInput(
						attrs={
							'type':'tel',
							'class':'form-control',
							'placeholder':'Phone Number',
							'id':'phone',
							'data-validation-required-message':'Please enter your phone number.',
						}),
					'message': forms.Textarea(
						attrs={
							'rows':'5',
							'class':'form-control',
							'placeholder':'Message',
							'id':'message',
							'data-validation-required-message':'Please enter a message.'
						}),
				}