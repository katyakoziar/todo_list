from django.test import TestCase
from django.urls import reverse
from todo.models import Task, Tag


class ViewsTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(content="Test Task")
        self.tag = Tag.objects.create(name="Test Tag")
        self.task.tags.add(self.tag)

    def test_task_list_view(self):
        response = self.client.get(reverse("todo:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_task_create_view(self):
        new_task = Task.objects.create(content="New Task")
        self.assertEqual(new_task.content, "New Task")

    def test_task_toggle_status_view(self):
        initial_status = self.task.is_completed
        response = self.client.post(reverse("todo:task_toggle_status", kwargs={"pk": self.task.pk}))
        self.assertEqual(response.status_code, 302)

        updated_task = Task.objects.get(pk=self.task.pk)
        self.assertNotEqual(initial_status, updated_task.is_completed)
