from django.urls import path
from .views import (
    IssueListView,
    IssueDetailView,
    IssueCreateView,
    IssueDeleteView,
    IssueUpdateView,
    MyIssuedListView,
    # UserProfileUpdateView,
    # UsersView,
    # DraftIssueListView,
    # ArchivedIssueListView,
)

urlpatterns = [
    path('', IssueListView.as_view(), name='issue_list'),
    path('<int:pk>', IssueDetailView.as_view(), name='issue_detail'),
    path('new/', IssueCreateView.as_view(), name='new'),
    path('<int:pk>/edit/', IssueUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', IssueDeleteView.as_view(), name='delete'),
    path('issued/', MyIssuedListView.as_view(), name='my_issued_list'),
    # path('user/<int:pk>/profile/', UserProfileUpdateView.as_view(), name='user_profile'),
]