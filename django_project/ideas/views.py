from django.shortcuts import render
from ideas.models import Idea

def create_idea():
    return ""

def get_ideas(id):
    first_idea = Idea.objects.all()
    get_ideas_with_id_greater_than_100 = Idea.objects.filter(id__gte=100, name="test")
    idea_with_id_1 = Idea.objects.get(id=1)
    Idea.objects.create(
        name="Test idea",
        description="Description"
    )

    idea_with_id_1.description = "updated_description"
    idea_with_id_1.name = "NEW NAME"
    idea_with_id_1.save()



    user_idea = Idea.objects.get(id=id)
    user_idea.name = form.name
    user_idea.description = form.description
    user_idea.save()

    user_idea.delete()

    first_idea.user_id.name
    return all_ideas
"select * from idea where id >= 100 and name='test'"