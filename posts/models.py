from django.db import models
from django.contrib.auth.models import User


class Post(models.model):
    """
    Post model related to the user (owner) instance
    """
    owner = models.ForeignKey(User, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    instrument = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    file = models.FileField(
        upload_to='../woodshed_media/pdfs/',
        blank=True,
        default='../woodshed_media/pdf-default_kpbimk.png',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
