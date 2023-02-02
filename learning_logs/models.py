from django.db import models


class Topic(models.Model):
    """A topic the user is learning about"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    # String representation of text field
    def __str__(self):
        return self.text


class Entry(models.Model):
    """Something specific learned about the topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    # Here user will write what he learned
    text = models.TextField()
    # adds record about date_time when topic was created
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) >= 50:
            return self.text[:50]
        else:
            return self.text

