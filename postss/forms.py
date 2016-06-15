from django import forms

from .models import Post

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