from django.test import TestCase
from todo.models import Tag, Task


class ModelsTests(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(
            name="Test Tag"
        )
        self.assertEqual(str(tag), tag.name)

    def test_task_str(self):
        tag = Tag.objects.create(
            name="Test Tag1"
        )
        task = Task.objects.create(
            content="Test Task",
            is_completed=False
        )
        task.tags.add(tag)
        self.assertEqual(str(task), f"{task.content} {task.is_completed}")
