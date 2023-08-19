from django.db import models


class Problem(models.Model):
    name = models.CharField(max_length=1024, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProblemSolution(models.Model):
    output = models.CharField(max_length=256)
    input = models.CharField(max_length=256)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="output_input")

    def __str__(self):
        return f"{self.output} {self.input}"
