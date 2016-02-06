from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from app.image.models import Image
from app.tag.models import Tag


# Project model
class Project(models.Model):
    title = models.TextField(max_length=512)
    name = models.TextField(max_length=512, unique=True)
    description = models.TextField(max_length=512, blank=True, null=True)
    url = models.TextField(max_length=1024, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    markdown = models.TextField(blank=True, null=True)
    type = models.IntegerField()
    images = models.ManyToManyField(Image, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField('date updated', auto_now=True, blank=True, null=True)
    created_user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)

    @staticmethod
    def validateJsonObject(jsonObject):

        try:
            nameField = jsonObject['name']
        except KeyError:
            return {'code': 'auth/noname'}, 404
        try:
            titleField = jsonObject['title']
        except KeyError:
            return {'code': 'auth/notitle'}, 404

        return {'code': 'ok'}, 200

    def updateFromJsonObject(self, jsonObject):
        self.title = jsonObject['title']
        self.name = jsonObject['name']
        self.description = jsonObject['description']
        self.url = jsonObject['url']
        self.text = jsonObject['text']
        self.html = jsonObject['html']
        self.markdown = jsonObject['markdown']
        self.type = jsonObject['type']

        # tags
        tagFieldIds = []
        tagFieldTexts = []
        for tag in jsonObject['tags']:
            try:
                tagId = tag['id']
            except KeyError:
                tagId = None
            try:
                tagText = tag['text']
            except KeyError:
                tagText = None
            if tagId is not None:
                tagFieldIds.append(tagId)
            if tagId is None and tagText is not None:
                tagFieldTexts.append(tag)


        for tag in self.tags.all():
            if tag.id not in tagFieldIds:
                self.tags.remove(tag)

        for tagText in tagFieldTexts:
            tag, tagCreated = Tag.objects.get_or_create(text=tagText['text'])
            self.tags.add(tag)

        # images
        imageFieldIds = []
        imageFieldSrcs = []
        for image in jsonObject['images']:
            try:
                imageId = int(image['id'])
            except:
                imageId = None

            try:
                imageSrc = image['src']
            except KeyError:
                imageSrc = None
            if imageId is not None:
                imageFieldIds.append(imageId)
            print imageId
            print imageSrc
            if imageId is None and imageSrc is not None:
                imageFieldSrcs.append(image)

        for image in self.images.all():
            if image.id not in imageFieldIds:
                self.images.remove(image)

        for imageSrc in imageFieldSrcs:
            image, imageCreated = Image.objects.get_or_create(src=imageSrc['src'])
            self.images.add(image)


        return {'code': 'ok'}, 200
