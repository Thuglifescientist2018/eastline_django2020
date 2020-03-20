from django.forms import ModelForm, ValidationError
from .models import BlogPost


class BlogPostModelForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ["topic", "slug", "write"]


    def __init__(self, *args, **kwargs):
        super(BlogPostModelForm, self).__init__(*args, **kwargs)
        self.fields['topic'].widget.attrs['placeholder'] = self.fields['topic'].label and 'Add topic for your Blog'
        self.fields['write'].widget.attrs['placeholder'] = self.fields['write'].label and 'Write your Blog here ... '

    def clean_topic(self, *args, **kwargs):
        instance = self.instance
        topic = self.cleaned_data.get("topic")
        qs = BlogPost.objects.filter(topic__iexact=topic)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise ValidationError("This Topic has been already Posted Please Try a new one. Try using words in a different way")
        return topic
            
       