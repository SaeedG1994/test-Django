from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProjectSerializers
from dev_projects.models import Project


@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializers = ProjectSerializers(projects,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getProject(request,pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializers(project,many=False)
    return Response(serializer.data)