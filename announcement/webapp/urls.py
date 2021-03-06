from django.urls import path
from webapp.views import AnnouncementListView, AnnouncementDetailView, AnnouncementUpdateView, AnnouncementCreateView, \
    announcement_delete_view, ModeratoringListView, CommentCreateView

app_name = 'webapp'

urlpatterns = [
    path('list/announcement/', AnnouncementListView.as_view(), name='list_announcement'),
    path('create/announcement', AnnouncementCreateView.as_view(), name='create_announcement'),
    path('delete/announcement/<int:pk>', announcement_delete_view, name='delete_announcement'),
    path('detail/announcement/<int:pk>', AnnouncementDetailView.as_view(), name='detail_announcement'),
    path('update/announcement/<int:pk>', AnnouncementUpdateView.as_view(), name='update_announcement'),
    path('list/to/moderate', ModeratoringListView.as_view(), name='list_to_moderator'),
    path('create/comment/<int:pk>', CommentCreateView.as_view(), name='comment_create')
]