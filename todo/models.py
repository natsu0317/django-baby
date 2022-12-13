from django.db import models
from django.utils import timezone

# Create your models here.
#Todoというモデルを作成　-->　データベースに保存される

class Todo(models.Model):
    #タイトル　-> 文字列、100文字まで
    title= models.CharField(max_length=100)
    #説明 -> 本文（文字列）、いっぱい書けるようにしたい
    description=models.TextField()
    #終わったか? -> チェックボックス
    created_by=models.ForeignKey('User',on_delete=models.CASCADE, null=True, blank=True,related_name='fuga')
    #on_deleteとは例えばUserに含まれている人が消えた時その人とひもづいているTodoは消すということ
    #もしPROTECTにするとその人が消えてもTodoは残る
    completed= models.BooleanField(default=False)
    #期限 -> 日付
    duedate=models.DateTimeField(blank=True, null=True)

    def __str__(self):
        #文字列にした時に、どんな表示にするか
        return self.title

class User(models.Model):
    name= models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name

#Userが1に対して、Todoが複数ある　->　一対多　-> ForeignKey
#Todoが1に対して、Tagは複数 & Tagが1に対してもTodoが複数 -> 多対多 -> ManyToManyField

class Tag(models.Model):
    name=models.CharField(max_length=100)
    todo=models.ManyToManyField(Todo,related_name='tags')
    #todoからtagを取る時に必要なのがrelated_name
    #views.pyの62行目

    def __str__(self):
        return self.name