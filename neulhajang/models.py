from django.db import models

from member.models import Member
from static_app.models import Category
from workspace.models import Period


# Create your models here.
class Neulhajang(Period):
    neulhajang_duration_start_date = models.DateField(null=True, blank=False)
    neulhajang_duration_end_date = models.DateField(null=True, blank=False)
    neulhajang_duration = models.IntegerField(null=False, blank=False, default=0)
    commitment_duration_start_date = models.DateField(null=False, blank=False)
    commitment_duration_end_date = models.DateField(null=False, blank=False)
    participants_target_amount = models.IntegerField(null=False, blank=False, default=0)
    promise_commit_content = models.TextField(null=False, blank=False)
    neulhajang_title = models.TextField(null=False, blank=False)
    thumnail_image = models.ImageField(null=False, blank=False, upload_to='neulhajang/thumbnail/')
    representing_tag = models.CharField(max_length=100, null=False, blank=False)
    participants_openchat_link = models.CharField(max_length=500,null=False, blank=False)
    neulhajang_status = models.CharField(max_length=100, null=False, blank=False)
    member = models.ForeignKey(Member, null=False, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, null=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbl_neulhajang'

class InnerPhoto(Period):
    inner_photo = models.ImageField(null=False, blank=False, upload_to='neulhajang/innerphoto/')
    neulhajang_content_order = models.IntegerField(null=False, blank=False, default=0)
    photo_explanation = models.CharField(max_length=300, null=False, blank=False)
    neulhajang = models.ForeignKey(Neulhajang, null=False, blank=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbl_inner_photo'

class NeulhajangMission(Period):
    mission_order = models.IntegerField(null=False, blank=False, default=0)
    mission_content = models.TextField(null=False, blank=False)
    neulhajang = models.ForeignKey(Neulhajang,null=False, blank=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbl_neulhajang_mission'

class NeulhajangInnerContent(Period):
    inner_content_text = models.TextField(null=False, blank=False)
    neulhajang_content_order = models.IntegerField(null=False,blank=False, default=0)
    neulhajang = models.ForeignKey(Neulhajang,null=False, blank=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbl_neulhajang_inner_content'

class NeulhajangInnerTitle(Period):
    inner_title_text = models.TextField(null=False, blank=False)
    neulhajang_content_order = models.IntegerField(null=False,blank=False, default=0)
    neulhajang = models.ForeignKey(Neulhajang,null=False, blank=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbl_neulhajang_inner_title'

class NeulhajangCommitment(Period):
    inner_title_text = models.TextField(null=False, blank=False)
    neulhajang = models.ForeignKey(Neulhajang,null=False, blank=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbl_neulhajang_commitment'

class CommitmentInnerPhotos(Period):
    inner_photo = models.ImageField(null=False, blank=False, upload_to='neulhajang/commitment_innerphoto/')
    photo_explanation = models.CharField(max_length=300, null=False, blank=False)
    commitment_content_order = models.IntegerField(null=False,blank=False, default=0)
    neulhajang = models.ForeignKey(Neulhajang,null=False, blank=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbl_commitment_inner_photos'

class CommitmentInnerContent(Period):
    inner_content_text = models.TextField(null=False, blank=False)
    commitment_content_order = models.IntegerField(null=False,blank=False, default=0)
    neulhajang = models.ForeignKey(Neulhajang,null=False, blank=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbl_commitment_inner_content'

class CommitmentInnerTitle(Period):
    inner_title_text = models.TextField(null=False, blank=False)
    commitment_content_order = models.IntegerField(null=False,blank=False, default=0)
    neulhajang = models.ForeignKey(Neulhajang,null=False, blank=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbl_commitment_inner_title'

class NeulhajangLike(Period):
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.DO_NOTHING)
    neulhajang = models.ForeignKey(Neulhajang, null=False, blank=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbl_neulhajang_like'

class NeulhajangAuthenticationFeed(Period):
    feedContent = models.TextField(null=False, blank=False)
    feedPhoto = models.ImageField(null=False, blank=False, upload_to='neulhajang/feedphoto/')
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.DO_NOTHING)
    neulhajang = models.ForeignKey(Neulhajang, null=False, blank=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbl_neulhajang_authentication_feed'
class AuthenticationFeedLike(Period):
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.DO_NOTHING)
    authentication_feed = models.ForeignKey(NeulhajangAuthenticationFeed, null=False, blank=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbl_authentication_feed_like'