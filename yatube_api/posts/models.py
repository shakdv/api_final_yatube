from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField(
        max_length=5000,
        help_text='Введите текст поста',
        verbose_name='Текст поста'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='Группа',
        help_text='Выберите группу'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='posts/',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'

    def __str__(self):
        return self.text


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='ЧПУ'
    )
    description = models.TextField(
        max_length=300,
        verbose_name='Описание'
    )

    class Meta:
        verbose_name_plural = 'Группы'
        verbose_name = 'Группу'

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    text = models.TextField(
        max_length=5000,
        verbose_name='Комментарий'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Создан'
    )

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'

    def __str__(self):
        return self.text


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Пользователь')
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор')

    class Meta:
        verbose_name_plural = 'Подписки'
        verbose_name = 'Подписка'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='following_unique'
            ),
        ]

    def __str__(self):
        return f'{self.user} подписан на {self.following}'
