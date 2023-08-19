from django.db import models
from users.models import UserModel
from problems.models import Problem


class Solution(models.Model):
    class LanguageType(models.TextChoices):
        PYTHON = "Python"
        C = "C"
        JAVA = "Java"
        PHP = "Php"

    code = models.CharField(max_length=1024)
    lang = models.CharField(max_length=32, choices=LanguageType.choices)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="problem")
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="solution")

    def __str__(self):
        return self.code
