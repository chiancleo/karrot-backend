# Generated by Django 2.1 on 2018-08-23 19:25

from django.db import migrations, models
import django.db.models.deletion


def set_latest_message(apps, schema_editor):
    Conversation = apps.get_model('conversations', 'Conversation')
    ConversationMessage = apps.get_model('conversations', 'ConversationMessage')

    for c in Conversation.objects.all():
        try:
            c.latest_message = c.messages.latest('id')
            c.save()
        except ConversationMessage.DoesNotExist:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0017_set_conversation_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='latest_message',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='conversation_latest_message',
                to='conversations.ConversationMessage'
            ),
        ),
        migrations.RunPython(set_latest_message, migrations.RunPython.noop, elidable=True)
    ]
