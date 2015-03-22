from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import MyUser, Region, Dialect, Vocabulary, VocabularyValidation
from .models import Skills, Interests
from django import forms


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = MyUser


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            MyUser.objects.get(username=username)
        except MyUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('skill', 'interests',)}),
    )


admin.site.register(MyUser, MyUserAdmin)


class RegionAdmin(admin.ModelAdmin):
    fields = ('name', 'shortdescription', 'superregion')
    list_display = ('name', 'shortdescription', 'superregion')


class VocabularyValidationAdmin(admin.ModelAdmin):
    fields = ('word', 'validated_by', 'validationborder')
    list_display = ('word', 'validationborder')


class DialectAdmin(admin.ModelAdmin):
    fields = ('name', 'region', 'superdialect')
    list_display = ('name', 'superdialect')


class SkillsAdmin(admin.ModelAdmin):
    fields = ('name')
    list_display = ('name')


class InterestsAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


class VocabularyAdmin(admin.ModelAdmin):
    fields = ('tibetan', 'english', 'german', 'pronounciation', 'validated', 'dialect', 'categories', 'notes')
    list_display = ('tibetan', 'english', 'german', 'pronounciation', 'validated')


admin.site.register(Region, RegionAdmin)
admin.site.register(VocabularyValidation, VocabularyValidationAdmin)
admin.site.register(Dialect, DialectAdmin)
admin.site.register(Vocabulary, VocabularyAdmin)
admin.site.register(Interests)
admin.site.register(Skills)