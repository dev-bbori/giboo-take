# Generated by Django 4.2.4 on 2023-08-16 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('static_app', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neulhajang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('neulhajang_duration_start_date', models.DateField(null=True)),
                ('neulhajang_duration_end_date', models.DateField(null=True)),
                ('neulhajang_duration', models.IntegerField(default=0)),
                ('commitment_duration_start_date', models.DateField()),
                ('commitment_duration_end_date', models.DateField()),
                ('participants_target_amount', models.IntegerField(default=0)),
                ('promise_commit_content', models.TextField()),
                ('neulhajang_title', models.TextField()),
                ('thumnail_image', models.ImageField(upload_to='neulhajang/thumbnail/')),
                ('representing_tag', models.CharField(max_length=100)),
                ('participants_openchat_link', models.CharField(max_length=500)),
                ('neulhajang_status', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='static_app.category')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='member.member')),
            ],
            options={
                'db_table': 'tbl_neulhajang',
            },
        ),
        migrations.CreateModel(
            name='NeulhajangMission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('mission_order', models.IntegerField(default=0)),
                ('mission_content', models.TextField()),
                ('neulhajang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='neulhajang.neulhajang')),
            ],
            options={
                'db_table': 'tbl_neulhajang_mission',
            },
        ),
        migrations.CreateModel(
            name='NeulhajangLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='member.member')),
                ('neulhajang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='neulhajang.neulhajang')),
            ],
            options={
                'db_table': 'tbl_neulhajang_like',
            },
        ),
        migrations.CreateModel(
            name='NeulhajangInnerTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('inner_title_text', models.TextField()),
                ('neulhajang_content_order', models.IntegerField(default=0)),
                ('neulhajang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='neulhajang.neulhajang')),
            ],
            options={
                'db_table': 'tbl_neulhajang_inner_title',
            },
        ),
        migrations.CreateModel(
            name='NeulhajangInnerContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('inner_content_text', models.TextField()),
                ('neulhajang_content_order', models.IntegerField(default=0)),
                ('neulhajang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='neulhajang.neulhajang')),
            ],
            options={
                'db_table': 'tbl_neulhajang_inner_content',
            },
        ),
        migrations.CreateModel(
            name='NeulhajangCommitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('inner_title_text', models.TextField()),
                ('neulhajang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='neulhajang.neulhajang')),
            ],
            options={
                'db_table': 'tbl_neulhajang_commitment',
            },
        ),
        migrations.CreateModel(
            name='NeulhajangAuthenticationFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('feedContent', models.TextField()),
                ('feedPhoto', models.ImageField(upload_to='neulhajang/feedphoto/')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='member.member')),
                ('neulhajang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='neulhajang.neulhajang')),
            ],
            options={
                'db_table': 'tbl_neulhajang_authentication_feed',
            },
        ),
        migrations.CreateModel(
            name='InnerPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('inner_photo', models.ImageField(upload_to='neulhajang/innerphoto/')),
                ('neulhajang_content_order', models.IntegerField(default=0)),
                ('photo_explanation', models.CharField(max_length=300)),
                ('neulhajang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='neulhajang.neulhajang')),
            ],
            options={
                'db_table': 'tbl_inner_photo',
            },
        ),
        migrations.CreateModel(
            name='CommitmentInnerTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('inner_title_text', models.TextField()),
                ('commitment_content_order', models.IntegerField(default=0)),
                ('neulhajang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='neulhajang.neulhajang')),
            ],
            options={
                'db_table': 'tbl_commitment_inner_title',
            },
        ),
        migrations.CreateModel(
            name='CommitmentInnerPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('inner_photo', models.ImageField(upload_to='neulhajang/commitment_innerphoto/')),
                ('photo_explanation', models.CharField(max_length=300)),
                ('commitment_content_order', models.IntegerField(default=0)),
                ('neulhajang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='neulhajang.neulhajang')),
            ],
            options={
                'db_table': 'tbl_commitment_inner_photos',
            },
        ),
        migrations.CreateModel(
            name='CommitmentInnerContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('inner_content_text', models.TextField()),
                ('commitment_content_order', models.IntegerField(default=0)),
                ('neulhajang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='neulhajang.neulhajang')),
            ],
            options={
                'db_table': 'tbl_commitment_inner_content',
            },
        ),
        migrations.CreateModel(
            name='AuthenticationFeedLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('authentication_feed', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='neulhajang.neulhajangauthenticationfeed')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='member.member')),
            ],
            options={
                'db_table': 'tbl_authentication_feed_like',
            },
        ),
    ]
