from django.db import models

# Create your models here.
#Todoというモデルを作成　-->　データベースに保存される

class Todo(models.Model):
    #タイトル　-> 文字列、100文字まで
    title= models.CharField(max_length=100)
    #説明 -> 本文（文字列）、いっぱい書けるようにしたい
    description=models.TextField()
    #終わったか? -> チェックボックス
    completed= models.BooleanField(default=False)
    #期限 -> 日付
    duedate=models.DateTimeField(blank=True, null=True)

    def __str__(self):
        #文字列にした時に、どんな表示にするか
        return self.title
