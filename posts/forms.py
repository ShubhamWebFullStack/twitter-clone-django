from django import forms
from posts.models import Post

# Form (all fields) validation & stored inside the Post Model using Django Form & ModelForm Class.
class PostForm(forms.ModelForm):
    # Meta Model Class is used to change the behavior of Model Fields like order_by, etc. It is completely optional to use Meta Class inside Model Class.
    class Meta:
        # Validation & Store the Data inside the Post DB Tables.
        model = Post
        fields = "__all__"
