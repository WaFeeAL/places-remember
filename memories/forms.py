from django.forms import ModelForm

from memories.models import MemoryModel


class MemoryForm(ModelForm):
    class Meta:
        model = MemoryModel
        fields = ('user', 'location_name', 'location_address', 'location_memories')
