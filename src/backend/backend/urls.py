from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework import routers
from django.views.generic import TemplateView
from togather.views import UserViewSet

router = routers.SimpleRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "schema",
        get_schema_view(
            title="Togather",
            description="A tinder-like app for creating new friendships and setting up group hangouts with random people",
        ),
        name="schema",
    ),
    path(
        "",
        TemplateView.as_view(
            template_name="togather/swagger-ui.html",
            extra_context={"schema_url": "schema"},
        ),
        name="swagger",
    ),
] + router.urls
